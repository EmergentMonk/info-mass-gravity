#!/usr/bin/env bash
# Repository Synchronization Script
# Clones repos from EmergentMonk and multimodalas organizations,
# creates TEST/DEV branches, and forks them to QSOLKCB with BUILD branches
#
# Authors: EmergentMonk/info-mass-gravity project
# Usage: ./repo_sync.sh [--dry-run] [--retry-count=N] [--verbose]

set -euo pipefail

# =============================================================================
# Configuration
# =============================================================================
ORG_TEST="EmergentMonk"
ORG_DEV="multimodalas"
ORG_BUILD="QSOLKCB"
TMPDIR="${HOME}/repo_mirror"

# Default settings
DRY_RUN=false
RETRY_COUNT=3
VERBOSE=false
FAILED_REPOS=()
PROCESSED_REPOS=()

# =============================================================================
# Utility Functions
# =============================================================================

# Log message with timestamp
log() {
    local level="$1"
    shift
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    case "$level" in
        "INFO")  echo "[$timestamp] ℹ️  $*" ;;
        "WARN")  echo "[$timestamp] ⚠️  $*" ;;
        "ERROR") echo "[$timestamp] ❌ $*" >&2 ;;
        "SUCCESS") echo "[$timestamp] ✅ $*" ;;
        "DEBUG") 
            if [[ "$VERBOSE" == true ]]; then
                echo "[$timestamp] 🔍 $*"
            fi
            ;;
    esac
}

# Show usage information
usage() {
    cat << EOF
Repository Synchronization Script

USAGE:
    $0 [OPTIONS]

OPTIONS:
    --dry-run           Only list repositories, don't perform actual operations
    --retry-count=N     Number of retry attempts for failed operations (default: 3)
    --verbose           Enable verbose debugging output
    --help             Show this help message

DESCRIPTION:
    This script performs the following operations:
    1. Clones all repositories from EmergentMonk organization to TEST branch
    2. Clones all repositories from multimodalas organization to DEV branch  
    3. Forks all repositories to QSOLKCB organization with BUILD branch

PREREQUISITES:
    - GitHub CLI (gh) must be installed and authenticated
    - Git must be installed and configured
    - SSH access to GitHub (for pushing to forks)
    - Sufficient permissions to fork repositories to target organization

EXAMPLES:
    # Dry run to see what would be processed
    $0 --dry-run
    
    # Normal execution with verbose output
    $0 --verbose
    
    # With custom retry count
    $0 --retry-count=5

EOF
}

# Parse command line arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dry-run)
                DRY_RUN=true
                shift
                ;;
            --retry-count=*)
                RETRY_COUNT="${1#*=}"
                # Validate retry count is a positive integer
                if ! [[ "$RETRY_COUNT" =~ ^[1-9][0-9]*$ ]]; then
                    log "ERROR" "Invalid retry count: $RETRY_COUNT. Must be a positive integer."
                    exit 1
                fi
                shift
                ;;
            --verbose)
                VERBOSE=true
                shift
                ;;
            --help)
                usage
                exit 0
                ;;
            *)
                log "ERROR" "Unknown option: $1"
                usage
                exit 1
                ;;
        esac
    done
}

# Check prerequisites
check_prerequisites() {
    log "INFO" "Checking prerequisites..."
    
    # Check if gh is installed and authenticated
    if ! command -v gh &> /dev/null; then
        log "ERROR" "GitHub CLI (gh) is not installed. Please install it first."
        exit 1
    fi
    
    if ! gh auth status &> /dev/null; then
        log "ERROR" "GitHub CLI is not authenticated. Run 'gh auth login' first."
        exit 1
    fi
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        log "ERROR" "Git is not installed. Please install it first."
        exit 1
    fi
    
    # Check git configuration
    if ! git config user.email &> /dev/null || ! git config user.name &> /dev/null; then
        log "WARN" "Git user configuration not set. This may cause issues."
        log "INFO" "Run 'git config --global user.email' and 'git config --global user.name'"
    fi
    
    log "SUCCESS" "All prerequisites satisfied"
}

# Retry wrapper for operations that might fail
retry_operation() {
    local operation_name="$1"
    local max_attempts="$RETRY_COUNT"
    local attempt=1
    shift
    
    while [[ $attempt -le $max_attempts ]]; do
        log "DEBUG" "Attempting $operation_name (attempt $attempt/$max_attempts)"
        
        if "$@"; then
            log "DEBUG" "$operation_name succeeded on attempt $attempt"
            return 0
        else
            local exit_code=$?
            log "WARN" "$operation_name failed on attempt $attempt (exit code: $exit_code)"
            
            if [[ $attempt -eq $max_attempts ]]; then
                log "ERROR" "$operation_name failed after $max_attempts attempts"
                return $exit_code
            fi
            
            # Exponential backoff: 2^attempt seconds
            local sleep_time=$((2 ** attempt))
            log "DEBUG" "Waiting ${sleep_time}s before retry..."
            sleep $sleep_time
            
            ((attempt++))
        fi
    done
}

# Get list of repositories from organization
get_repo_list() {
    local org="$1"
    local repos
    
    log "INFO" "Fetching repository list from organization: $org"
    
    # Use gh to get repository list, with error handling
    if repos=$(gh repo list "$org" --limit 200 --json name -q '.[].name' 2>/dev/null); then
        local repo_count
        if [[ -z "$repos" ]]; then
            repo_count=0
        else
            repo_count=$(echo "$repos" | wc -l)
        fi
        log "INFO" "Found $repo_count repositories in $org"
        echo "$repos"
    else
        log "ERROR" "Failed to fetch repositories from organization: $org"
        log "ERROR" "Please check organization name and your access permissions"
        return 1
    fi
}

# Check if branch exists in repository
branch_exists() {
    local branch="$1"
    git rev-parse --verify "$branch" &>/dev/null
}

# Check if remote branch exists
remote_branch_exists() {
    local remote="$1"
    local branch="$2"
    git ls-remote --heads "$remote" "$branch" | grep -q "$branch"
}

# Process a single repository
process_repository() {
    local org="$1"
    local repo="$2" 
    local target_branch="$3"
    local repo_dir="$repo"
    
    log "INFO" "=== Processing $org/$repo → branch $target_branch ==="
    
    # Skip if already processed (for resume capability)
    if [[ -d "$repo_dir" ]] && [[ " ${PROCESSED_REPOS[*]} " =~ " ${org}/${repo} " ]]; then
        log "INFO" "Repository $org/$repo already processed, skipping..."
        return 0
    fi
    
    # Clone repository if it doesn't exist
    if [[ ! -d "$repo_dir" ]]; then
        log "INFO" "Cloning repository $org/$repo..."
        if [[ "$DRY_RUN" == true ]]; then
            log "INFO" "DRY RUN: Would clone $org/$repo"
        else
            if ! retry_operation "clone $org/$repo" gh repo clone "$org/$repo" "$repo_dir"; then
                log "ERROR" "Failed to clone $org/$repo"
                FAILED_REPOS+=("CLONE:$org/$repo")
                return 1
            fi
        fi
    else
        log "INFO" "Repository directory $repo_dir already exists"
    fi
    
    if [[ "$DRY_RUN" == false ]]; then
        cd "$repo_dir"
        
        # Fetch latest changes
        log "DEBUG" "Fetching latest changes..."
        retry_operation "fetch origin" git fetch origin
        
        # Check if target branch exists locally or remotely
        if branch_exists "$target_branch"; then
            log "INFO" "Branch $target_branch exists locally, checking out..."
            git checkout "$target_branch"
            if remote_branch_exists "origin" "$target_branch"; then
                log "DEBUG" "Pulling latest changes from origin/$target_branch"
                retry_operation "pull $target_branch" git pull origin "$target_branch"
            fi
        elif remote_branch_exists "origin" "$target_branch"; then
            log "INFO" "Branch $target_branch exists on remote, checking out..."
            git checkout -b "$target_branch" "origin/$target_branch"
        else
            log "INFO" "Creating new branch $target_branch..."
            git checkout -b "$target_branch"
            log "INFO" "Pushing new branch $target_branch to origin..."
            if ! retry_operation "push new branch" git push origin "$target_branch"; then
                log "ERROR" "Failed to push new branch $target_branch"
                FAILED_REPOS+=("PUSH:$org/$repo:$target_branch")
                cd ..
                return 1
            fi
        fi
        
        # Fork repository to build organization
        log "INFO" "Forking $org/$repo into $ORG_BUILD..."
        if ! gh repo view "$ORG_BUILD/$repo" &>/dev/null; then
            if ! retry_operation "fork repository" gh repo fork "$org/$repo" --org "$ORG_BUILD" --remote=false; then
                log "ERROR" "Failed to fork $org/$repo to $ORG_BUILD"
                FAILED_REPOS+=("FORK:$org/$repo")
                cd ..
                return 1
            fi
        else
            log "INFO" "Fork $ORG_BUILD/$repo already exists"
        fi
        
        # Add build remote if it doesn't exist
        if ! git remote get-url build &>/dev/null; then
            log "DEBUG" "Adding build remote..."
            if ! git remote add build "git@github.com:$ORG_BUILD/$repo.git"; then
                log "WARN" "Failed to add build remote for unknown reason"
            fi
        else
            log "DEBUG" "Build remote already exists, updating URL..."
            git remote set-url build "git@github.com:$ORG_BUILD/$repo.git"
        fi
        
        # Push to build organization as BUILD branch
        log "INFO" "Pushing $target_branch to $ORG_BUILD/$repo as BUILD branch..."
        if ! retry_operation "push to build remote" git push build "$target_branch:BUILD"; then
            log "ERROR" "Failed to push to build remote for $repo"
            FAILED_REPOS+=("PUSH_BUILD:$org/$repo")
            cd ..
            return 1
        fi
        
        cd ..
    fi
    
    PROCESSED_REPOS+=("$org/$repo")
    log "SUCCESS" "Successfully processed $org/$repo"
    return 0
}

# Process all repositories from an organization
process_organization() {
    local org="$1"
    local target_branch="$2"
    local repos
    local total_repos=0
    local successful_repos=0
    local failed_repos=0
    
    log "INFO" "Starting processing for organization: $org (target branch: $target_branch)"
    
    # Get repository list
    if ! repos=$(get_repo_list "$org"); then
        log "ERROR" "Failed to get repository list for $org"
        return 1
    fi
    
    if [[ -z "$repos" ]]; then
        log "WARN" "No repositories found in organization $org"
        return 0
    fi
    
    # Process each repository
    while IFS= read -r repo; do
        [[ -z "$repo" ]] && continue
        
        ((total_repos++))
        log "INFO" "Processing repository $total_repos: $repo"
        
        if process_repository "$org" "$repo" "$target_branch"; then
            ((successful_repos++))
        else
            ((failed_repos++))
        fi
        
        log "DEBUG" "Progress: $successful_repos successful, $failed_repos failed out of $total_repos total"
    done <<< "$repos"
    
    log "INFO" "Completed processing $org: $successful_repos/$total_repos repositories successful"
    
    if [[ $failed_repos -gt 0 ]]; then
        log "WARN" "$failed_repos repositories failed for organization $org"
        return 1
    fi
    
    return 0
}

# Print final summary
print_summary() {
    local total_processed=${#PROCESSED_REPOS[@]}
    local total_failed=${#FAILED_REPOS[@]}
    
    echo
    log "INFO" "=== FINAL SUMMARY ==="
    log "INFO" "Total repositories processed: $total_processed"
    log "INFO" "Total repositories failed: $total_failed"
    
    if [[ $total_failed -gt 0 ]]; then
        log "WARN" "Failed operations:"
        for failed in "${FAILED_REPOS[@]}"; do
            log "WARN" "  $failed"
        done
    fi
    
    if [[ $total_failed -eq 0 ]]; then
        log "SUCCESS" "✅ All repositories processed successfully!"
    else
        log "WARN" "⚠️  Some repositories failed processing. Check logs above for details."
    fi
    
    log "INFO" "Repository mirror location: $TMPDIR"
}

# =============================================================================
# Main Execution
# =============================================================================

main() {
    echo "Repository Synchronization Script"
    echo "================================="
    echo
    
    # Parse command line arguments
    parse_args "$@"
    
    # Show configuration
    log "INFO" "Configuration:"
    log "INFO" "  Source TEST org: $ORG_TEST"
    log "INFO" "  Source DEV org: $ORG_DEV" 
    log "INFO" "  Target BUILD org: $ORG_BUILD"
    log "INFO" "  Mirror directory: $TMPDIR"
    log "INFO" "  Dry run: $DRY_RUN"
    log "INFO" "  Retry count: $RETRY_COUNT"
    log "INFO" "  Verbose: $VERBOSE"
    echo
    
    # Check prerequisites
    check_prerequisites
    
    # Create and enter working directory
    log "INFO" "Setting up working directory: $TMPDIR"
    mkdir -p "$TMPDIR"
    cd "$TMPDIR"
    
    # Process organizations
    local overall_success=true
    
    if ! process_organization "$ORG_TEST" "TEST"; then
        overall_success=false
    fi
    
    if ! process_organization "$ORG_DEV" "DEV"; then
        overall_success=false
    fi
    
    # Print final summary
    print_summary
    
    if [[ "$overall_success" == true ]]; then
        exit 0
    else
        exit 1
    fi
}

# Handle script interruption gracefully
trap 'log "WARN" "Script interrupted. Partial progress saved in $TMPDIR"; exit 130' INT TERM

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi