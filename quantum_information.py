"""
Quantum Information Theory Module

This module implements foundational quantum information concepts including
entropy, entanglement, and information-theoretic measures.

CITATIONS:
- Trent Slade: Informational Mass Gravity Framework
- Gary Vetro: Informational Mass Gravity Framework
- Melvin Vopson: Mass-energy-information equivalence principle
- Erik Verlinde: Entropic gravity and emergent spacetime

Provenance: Open Science Initiative
License: Open source for educational and research purposes
Ethics: This code is intended for theoretical exploration and education.
        Users must consider implications of quantum information research.
"""

import numpy as np
from typing import Tuple, Optional
import warnings


def von_neumann_entropy(density_matrix: np.ndarray) -> float:
    """
    Calculate the von Neumann entropy of a quantum state.
    
    S(ρ) = -Tr(ρ log₂ ρ)
    
    This fundamental measure quantifies quantum information content,
    connecting to Vopson's mass-energy-information equivalence.
    
    Args:
        density_matrix: Density matrix representation of quantum state
        
    Returns:
        Von Neumann entropy in bits
        
    References:
        - Vopson, M. M. (2019). The mass-energy-information equivalence principle
        - Verlinde, E. (2011). On the origin of gravity and the laws of Newton
    """
    # Ensure hermitian
    if not np.allclose(density_matrix, density_matrix.conj().T):
        warnings.warn("Density matrix is not Hermitian, symmetrizing...")
        density_matrix = (density_matrix + density_matrix.conj().T) / 2
    
    # Get eigenvalues
    eigenvalues = np.linalg.eigvalsh(density_matrix)
    
    # Filter out zero/negative eigenvalues (numerical errors)
    eigenvalues = eigenvalues[eigenvalues > 1e-12]
    
    # Calculate entropy
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    
    return entropy


def quantum_mutual_information(rho_AB: np.ndarray, 
                               dim_A: int, 
                               dim_B: int) -> float:
    """
    Calculate quantum mutual information between subsystems A and B.
    
    I(A:B) = S(A) + S(B) - S(AB)
    
    Measures quantum correlations, relevant to Slade-Vetro framework
    of informational mass interactions.
    
    Args:
        rho_AB: Joint density matrix of system AB
        dim_A: Dimension of subsystem A
        dim_B: Dimension of subsystem B
        
    Returns:
        Quantum mutual information in bits
    """
    # Reduced density matrices
    rho_A = partial_trace(rho_AB, dim_A, dim_B, trace_over='B')
    rho_B = partial_trace(rho_AB, dim_A, dim_B, trace_over='A')
    
    # Calculate entropies
    S_A = von_neumann_entropy(rho_A)
    S_B = von_neumann_entropy(rho_B)
    S_AB = von_neumann_entropy(rho_AB)
    
    return S_A + S_B - S_AB


def partial_trace(rho: np.ndarray, 
                  dim_A: int, 
                  dim_B: int, 
                  trace_over: str = 'B') -> np.ndarray:
    """
    Compute partial trace over subsystem.
    
    Essential for analyzing quantum correlations in composite systems,
    relevant to emergent gravity models (Verlinde).
    
    Args:
        rho: Density matrix of composite system
        dim_A: Dimension of subsystem A
        dim_B: Dimension of subsystem B
        trace_over: Which subsystem to trace over ('A' or 'B')
        
    Returns:
        Reduced density matrix
    """
    rho_reshaped = rho.reshape(dim_A, dim_B, dim_A, dim_B)
    
    if trace_over == 'B':
        # Trace over B
        rho_reduced = np.trace(rho_reshaped, axis1=1, axis2=3)
    else:
        # Trace over A
        rho_reduced = np.trace(rho_reshaped, axis1=0, axis2=2)
    
    return rho_reduced


def entanglement_entropy(rho_AB: np.ndarray, 
                        dim_A: int, 
                        dim_B: int) -> float:
    """
    Calculate entanglement entropy between subsystems.
    
    Measures quantum entanglement, connecting to Verlinde's holographic
    principle and entropic force ideas.
    
    Args:
        rho_AB: Joint density matrix
        dim_A: Dimension of subsystem A
        dim_B: Dimension of subsystem B
        
    Returns:
        Entanglement entropy in bits
        
    References:
        - Verlinde, E. (2011). Entropic force and gravity
        - Slade, T. & Vetro, G.: Information-mass correspondence
    """
    rho_A = partial_trace(rho_AB, dim_A, dim_B, trace_over='B')
    return von_neumann_entropy(rho_A)


def quantum_fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
    """
    Calculate quantum fidelity between two density matrices.
    
    F(ρ,σ) = Tr(√(√ρ σ √ρ))²
    
    Measures distinguishability of quantum states, relevant for
    information-theoretic approaches to mass and gravity.
    
    Args:
        rho: First density matrix
        sigma: Second density matrix
        
    Returns:
        Fidelity value between 0 and 1
    """
    sqrt_rho = np.linalg.matrix_power(rho, 0.5)
    M = sqrt_rho @ sigma @ sqrt_rho
    sqrt_M = np.linalg.matrix_power(M, 0.5)
    fidelity = np.trace(sqrt_M) ** 2
    
    return np.real(fidelity)


def create_bell_state(which: int = 0) -> np.ndarray:
    """
    Create one of the four Bell states (maximally entangled states).
    
    These states are fundamental to quantum information and demonstrate
    the quantum correlations central to emergent gravity theories.
    
    Args:
        which: Which Bell state (0-3)
            0: |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
            1: |Φ⁻⟩ = (|00⟩ - |11⟩)/√2
            2: |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
            3: |Ψ⁻⟩ = (|01⟩ - |10⟩)/√2
            
    Returns:
        4x4 density matrix of Bell state
    """
    # State vectors
    if which == 0:
        psi = np.array([1, 0, 0, 1]) / np.sqrt(2)
    elif which == 1:
        psi = np.array([1, 0, 0, -1]) / np.sqrt(2)
    elif which == 2:
        psi = np.array([0, 1, 1, 0]) / np.sqrt(2)
    else:
        psi = np.array([0, 1, -1, 0]) / np.sqrt(2)
    
    # Density matrix
    rho = np.outer(psi, psi.conj())
    
    return rho


if __name__ == "__main__":
    # Demonstration of quantum information measures
    print("=" * 70)
    print("Quantum Information Theory Demonstrations")
    print("Framework by Trent Slade & Gary Vetro")
    print("Citations: Melvin Vopson, Erik Verlinde")
    print("=" * 70)
    
    # Bell state analysis
    bell_state = create_bell_state(0)
    print(f"\nBell State |Φ⁺⟩:")
    print(f"Joint entropy: {von_neumann_entropy(bell_state):.6f} bits")
    print(f"Entanglement entropy: {entanglement_entropy(bell_state, 2, 2):.6f} bits")
    
    # Mixed state
    mixed = 0.5 * create_bell_state(0) + 0.5 * np.eye(4) / 4
    print(f"\nMixed State:")
    print(f"Entropy: {von_neumann_entropy(mixed):.6f} bits")
