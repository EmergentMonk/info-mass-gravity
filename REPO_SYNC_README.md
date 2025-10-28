# Repository Synchronization Script

A comprehensive Bash script for synchronizing repositories across multiple GitHub organizations with automated branching and forking capabilities.

## Overview

This script automates the process of:
1. **Cloning** all repositories from the `EmergentMonk` organization and creating/updating `TEST` branches
2. **Cloning** all repositories from the `multimodalas` organization and creating/updating `DEV` branches  
3. **Forking** all repositories to the `QSOLKCB` organization and pushing both `TEST` and `DEV` branches as `BUILD` branches

## Features

### ✅ Core Functionality
- **Automated repository discovery** using GitHub CLI
- **Branch management** with automatic creation and updates
- **Repository forking** to target organization
- **Progress tracking** with detailed logging

### 🛡️ Robust Error Handling
- **Strict error handling** with `set -euo pipefail`
- **Retry logic** with exponential backoff for failed operations
- **Graceful skipping** of already-processed repositories
- **Comprehensive failure reporting** and recovery

### 📊 Enhanced Logging
- **Timestamped log messages** with severity levels
- **Progress indicators** with emoji markers
- **Verbose debugging mode** for troubleshooting
- **Final summary report** with success/failure statistics

### 🔧 Advanced Options
- **Dry-run mode** for safe testing
- **Configurable retry attempts** for network resilience
- **Resume capability** for interrupted operations
- **Prerequisite validation** before execution

## Prerequisites

### Required Tools
```bash
# GitHub CLI (required for repository operations)
# Install from: https://cli.github.com/
gh --version

# Git (required for repository management)
git --version

# Bash 4.0+ (required for advanced features)
bash --version
```

### GitHub Authentication
```bash
# Authenticate with GitHub CLI
gh auth login

# Verify authentication
gh auth status
```

### SSH Configuration
Ensure SSH access to GitHub is configured for pushing to forked repositories:
```bash
# Test SSH connection
ssh -T git@github.com

# If not configured, generate SSH key:
ssh-keygen -t ed25519 -C "your_email@example.com"
# Then add the public key to your GitHub account
```

### Permissions Required
- **Read access** to source organizations (`EmergentMonk`, `multimodalas`)
- **Fork permissions** to target organization (`QSOLKCB`)
- **Push access** to forked repositories

## Installation

1. **Download the script:**
```bash
curl -O https://raw.githubusercontent.com/EmergentMonk/info-mass-gravity/main/repo_sync.sh
chmod +x repo_sync.sh
```

2. **Verify prerequisites:**
```bash
./repo_sync.sh --help
```

## Usage

### Basic Usage
```bash
# Standard execution
./repo_sync.sh

# Dry run to preview operations
./repo_sync.sh --dry-run

# Verbose output for debugging
./repo_sync.sh --verbose

# Custom retry attempts
./repo_sync.sh --retry-count=5
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--dry-run` | Only list repositories, don't perform operations | `false` |
| `--retry-count=N` | Number of retry attempts for failed operations | `3` |
| `--verbose` | Enable detailed debugging output | `false` |
| `--help` | Show usage information | - |

### Example Workflows

#### 1. Safe Testing (Recommended First Run)
```bash
# Preview what will be processed
./repo_sync.sh --dry-run --verbose

# Review the output, then run for real
./repo_sync.sh --verbose
```

#### 2. Automated CI/CD Integration
```bash
#!/bin/bash
# ci-sync.sh - Automated synchronization
set -e

# Run with retry logic for CI environments
./repo_sync.sh --retry-count=5 --verbose

# Check exit code
if [ $? -eq 0 ]; then
    echo "✅ Repository sync completed successfully"
else
    echo "❌ Repository sync failed"
    exit 1
fi
```

#### 3. Recovery from Partial Failures
```bash
# The script automatically resumes from where it left off
# Just run it again if it was interrupted
./repo_sync.sh --verbose
```

## Configuration

### Environment Variables
You can customize the script behavior by modifying these variables at the top of the script:

```bash
# Source organizations
ORG_TEST="EmergentMonk"      # Creates TEST branches
ORG_DEV="multimodalas"       # Creates DEV branches

# Target organization  
ORG_BUILD="QSOLKCB"          # Receives BUILD branches

# Working directory
TMPDIR="${HOME}/repo_mirror" # Local repository storage
```

### Directory Structure
The script creates the following structure:
```
${HOME}/repo_mirror/
├── repo1/
│   ├── .git/
│   └── (repository contents)
├── repo2/
│   ├── .git/
│   └── (repository contents)
└── ...
```

## Output and Logging

### Log Levels
- **ℹ️ INFO**: General information and progress
- **⚠️ WARN**: Non-fatal warnings and issues  
- **❌ ERROR**: Serious errors requiring attention
- **✅ SUCCESS**: Successful operations
- **🔍 DEBUG**: Detailed debugging (with `--verbose`)

### Sample Output
```
Repository Synchronization Script
=================================

[2024-10-28 17:55:00] ℹ️  Configuration:
[2024-10-28 17:55:00] ℹ️    Source TEST org: EmergentMonk
[2024-10-28 17:55:00] ℹ️    Source DEV org: multimodalas
[2024-10-28 17:55:00] ℹ️    Target BUILD org: QSOLKCB
[2024-10-28 17:55:00] ℹ️    Mirror directory: /home/user/repo_mirror
[2024-10-28 17:55:00] ℹ️    Dry run: false
[2024-10-28 17:55:00] ℹ️    Retry count: 3

[2024-10-28 17:55:01] ✅ All prerequisites satisfied
[2024-10-28 17:55:01] ℹ️  Fetching repository list from organization: EmergentMonk
[2024-10-28 17:55:02] ℹ️  Found 5 repositories in EmergentMonk
[2024-10-28 17:55:02] ℹ️  === Processing EmergentMonk/repo1 → branch TEST ===
[2024-10-28 17:55:05] ✅ Successfully processed EmergentMonk/repo1

[2024-10-28 17:55:30] ℹ️  === FINAL SUMMARY ===
[2024-10-28 17:55:30] ℹ️  Total repositories processed: 10
[2024-10-28 17:55:30] ℹ️  Total repositories failed: 0
[2024-10-28 17:55:30] ✅ ✅ All repositories processed successfully!
```

## Error Handling and Troubleshooting

### Common Issues

#### 1. Authentication Problems
```bash
# Error: GitHub CLI not authenticated
# Solution:
gh auth login
gh auth status
```

#### 2. SSH Access Issues
```bash
# Error: Permission denied (publickey)
# Solution: Configure SSH keys
ssh-keygen -t ed25519 -C "your_email@example.com"
# Add public key to GitHub account
```

#### 3. Organization Access
```bash
# Error: Failed to fetch repositories
# Solution: Verify organization names and access permissions
gh repo list EmergentMonk --limit 1  # Test access
```

#### 4. Fork Permissions
```bash
# Error: Failed to fork repository
# Solution: Ensure you have permissions to fork to target organization
gh repo view QSOLKCB/test-repo  # Test target org access
```

### Recovery Procedures

#### Partial Failure Recovery
The script maintains state and can resume from interruptions:
```bash
# If script was interrupted, simply run again
./repo_sync.sh --verbose

# Check logs for specific failure details
grep "ERROR\|WARN" /path/to/logfile
```

#### Manual Cleanup
```bash
# Remove local mirror to start fresh
rm -rf ${HOME}/repo_mirror

# Or remove specific problematic repository
rm -rf ${HOME}/repo_mirror/problematic-repo
```

## Advanced Usage

### Custom Organization Synchronization
To sync different organizations, modify the script variables:
```bash
# Edit the script or create a custom version
ORG_TEST="your-source-org"
ORG_DEV="your-dev-org"  
ORG_BUILD="your-target-org"
```

### Integration with CI/CD
```yaml
# GitHub Actions example
name: Repository Sync
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Setup GitHub CLI
      run: |
        gh auth login --with-token <<< "${{ secrets.GH_TOKEN }}"
    - name: Run sync
      run: |
        ./repo_sync.sh --retry-count=5 --verbose
```

### Monitoring and Alerting
```bash
# Example monitoring script
#!/bin/bash
LOG_FILE="/var/log/repo-sync.log"

./repo_sync.sh --verbose 2>&1 | tee "$LOG_FILE"

if [ ${PIPESTATUS[0]} -ne 0 ]; then
    # Send alert (email, Slack, etc.)
    echo "Repository sync failed - check $LOG_FILE" | mail -s "Sync Failure" admin@company.com
fi
```

## Security Considerations

### Token Management
- Store GitHub tokens securely (environment variables, secret management)
- Use tokens with minimal required permissions
- Rotate tokens regularly

### SSH Key Security  
- Use SSH keys with passphrases
- Limit SSH key scope to necessary repositories
- Regularly audit SSH key access

### Network Security
- Run script from trusted networks
- Consider VPN for sensitive operations
- Monitor for suspicious repository access

## Performance Optimization

### Large Organization Handling
```bash
# For organizations with 200+ repositories, consider:
# 1. Parallel processing (modify script)
# 2. Incremental updates
# 3. Filtering specific repositories

# Example: Process only recently updated repos
gh repo list ORG --json name,updatedAt --limit 1000 | \
jq -r '.[] | select(.updatedAt > "2024-01-01") | .name'
```

### Resource Management
```bash
# Monitor disk space in mirror directory
df -h ${HOME}/repo_mirror

# Clean up old repositories periodically
find ${HOME}/repo_mirror -type d -name ".git" -execdir pwd \; | \
while read repo; do
  cd "$repo"
  # Clean up old branches, optimize repository
  git gc --aggressive
done
```

## Contributing

### Bug Reports
Please include:
- Script version and configuration
- Complete error messages and logs
- Environment details (OS, Git version, etc.)
- Steps to reproduce

### Feature Requests
- Describe the use case and benefit
- Provide example configuration or usage
- Consider backward compatibility

### Development
```bash
# Test changes safely
./repo_sync.sh --dry-run --verbose

# Validate script syntax
bash -n repo_sync.sh
shellcheck repo_sync.sh  # If available
```

## License

This script is part of the EmergentMonk/info-mass-gravity project and follows the same licensing terms.

## Support

For issues and questions:
1. Check this README for common solutions
2. Review script logs with `--verbose` flag
3. Test with `--dry-run` to isolate issues
4. Open an issue in the repository with detailed information

---

**Last Updated**: October 28, 2024  
**Script Version**: 1.0.0  
**Compatibility**: Bash 4.0+, GitHub CLI 2.0+, Git 2.0+