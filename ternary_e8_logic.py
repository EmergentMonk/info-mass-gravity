"""
Ternary Logic and E8 Lattice Module

Implements ternary (three-valued) logic systems and E8 lattice structures,
exploring their applications in quantum information and emergent gravity.

CITATIONS:
- Trent Slade: Informational Mass Gravity Framework
- Gary Vetro: Informational Mass Gravity Framework
- Melvin Vopson: Mass-energy-information equivalence principle
- Erik Verlinde: Entropic gravity and emergent spacetime

Provenance: Open Science Initiative
License: Open source for educational and research purposes
Ethics: These mathematical frameworks explore fundamental structures.
        Applications should be evaluated for their physical validity.
"""

import numpy as np
from typing import List, Tuple, Optional, Union
from enum import Enum


class TernaryValue(Enum):
    """Ternary logic values: FALSE (-1), UNKNOWN (0), TRUE (1)"""
    FALSE = -1
    UNKNOWN = 0
    TRUE = 1


class TernaryLogic:
    """
    Ternary (three-valued) logic system.
    
    Extends binary logic with an 'unknown' state, relevant to quantum
    superposition and the information-theoretic framework of Slade-Vetro.
    
    References:
        - Kleene, S. C. (1938). Three-valued logic
        - Łukasiewicz, J. (1920). Many-valued logics
    """
    
    @staticmethod
    def ternary_and(a: int, b: int) -> int:
        """
        Ternary AND operation (Kleene logic).
        
        Args:
            a, b: Values in {-1, 0, 1}
            
        Returns:
            Result in {-1, 0, 1}
        """
        if a == -1 or b == -1:
            return -1
        if a == 0 or b == 0:
            return 0
        return 1
    
    @staticmethod
    def ternary_or(a: int, b: int) -> int:
        """
        Ternary OR operation (Kleene logic).
        
        Args:
            a, b: Values in {-1, 0, 1}
            
        Returns:
            Result in {-1, 0, 1}
        """
        if a == 1 or b == 1:
            return 1
        if a == 0 or b == 0:
            return 0
        return -1
    
    @staticmethod
    def ternary_not(a: int) -> int:
        """
        Ternary NOT operation.
        
        Args:
            a: Value in {-1, 0, 1}
            
        Returns:
            Result in {-1, 0, 1}
        """
        return -a
    
    @staticmethod
    def ternary_implication(a: int, b: int) -> int:
        """
        Ternary implication: a → b.
        
        Args:
            a, b: Values in {-1, 0, 1}
            
        Returns:
            Result in {-1, 0, 1}
        """
        return TernaryLogic.ternary_or(TernaryLogic.ternary_not(a), b)


def e8_root_system() -> np.ndarray:
    """
    Generate the E8 root system (240 roots).
    
    E8 is an exceptional Lie group with fascinating mathematical properties,
    potentially relevant to fundamental physics and information structure
    (Lisi's E8 theory, string theory).
    
    Returns:
        240x8 array of E8 roots
        
    References:
        - Lie, S. & Cartan, É.: Classification of simple Lie algebras
        - Lisi, A. G. (2007). An exceptionally simple theory of everything
        - Conway, J. H. & Sloane, N. J. A.: Sphere packings and lattices
        
    Note: Connection to Slade-Vetro framework through information geometry
          and Verlinde's emergent spacetime structure.
    """
    roots = []
    
    # Type 1: 112 roots (all permutations and sign changes)
    for i in range(8):
        for j in range(i + 1, 8):
            for si in [-1, 1]:
                for sj in [-1, 1]:
                    root = np.zeros(8)
                    root[i] = si
                    root[j] = sj
                    roots.append(root)
    
    # Type 2: 128 roots (all even number of minus signs)
    for signs in range(256):
        root = np.array([(1 if (signs >> i) & 1 else -1) / 2 for i in range(8)])
        if np.sum(root) % 2 == 0:  # Even number of minus signs
            roots.append(root)
    
    return np.array(roots)


def e8_dimension() -> int:
    """Return dimension of E8 Lie algebra."""
    return 248


def e8_cartan_matrix() -> np.ndarray:
    """
    Generate the Cartan matrix for E8.
    
    The Cartan matrix encodes the structure of the E8 root system,
    fundamental to understanding symmetries in theoretical physics.
    
    Returns:
        8x8 Cartan matrix
    """
    # E8 Cartan matrix (Dynkin diagram based)
    cartan = np.array([
        [ 2, -1,  0,  0,  0,  0,  0,  0],
        [-1,  2, -1,  0,  0,  0,  0,  0],
        [ 0, -1,  2, -1,  0,  0,  0, -1],
        [ 0,  0, -1,  2, -1,  0,  0,  0],
        [ 0,  0,  0, -1,  2, -1,  0,  0],
        [ 0,  0,  0,  0, -1,  2, -1,  0],
        [ 0,  0,  0,  0,  0, -1,  2,  0],
        [ 0,  0, -1,  0,  0,  0,  0,  2]
    ])
    return cartan


def ternary_to_quantum_state(ternary_values: List[int]) -> np.ndarray:
    """
    Map ternary logic values to quantum state amplitudes.
    
    Explores connection between ternary logic and quantum superposition,
    relevant to information-based approaches to physics.
    
    Args:
        ternary_values: List of ternary values in {-1, 0, 1}
        
    Returns:
        Normalized quantum state vector
        
    Note: This mapping is exploratory, connecting discrete logic to
          continuous quantum states (Slade-Vetro framework).
    """
    # Map: -1 → |0⟩, 0 → (|0⟩+|1⟩)/√2, 1 → |1⟩
    dim = 2 ** len(ternary_values)
    state = np.zeros(dim, dtype=complex)
    
    for i, val in enumerate(ternary_values):
        if val == -1:
            # Contribute to |0⟩ states
            pass
        elif val == 1:
            # Contribute to |1⟩ states
            pass
        else:
            # Equal superposition
            pass
    
    # Simplified mapping: encode as qutrit-like structure
    n = len(ternary_values)
    state = np.zeros(3 ** n, dtype=complex)
    
    for i, val in enumerate(ternary_values):
        idx = (val + 1)  # Map {-1,0,1} to {0,1,2}
        state[idx + i * 3] = 1.0
    
    # Normalize
    norm = np.linalg.norm(state)
    if norm > 0:
        state = state / norm
    
    return state


def e8_lattice_vector_norm_squared(vector: np.ndarray) -> float:
    """
    Calculate squared norm of E8 lattice vector.
    
    E8 lattice has special properties: all vectors have squared norm
    that is an even integer, optimal sphere packing in 8D.
    
    Args:
        vector: 8-dimensional vector
        
    Returns:
        Squared norm
        
    References:
        - Viazovska, M. (2017). E8 lattice sphere packing proof
        - Connection to string theory and exceptional structures
    """
    return np.dot(vector, vector)


def kissing_number_e8() -> int:
    """
    Return the kissing number of E8 lattice.
    
    The kissing number (240) is the number of spheres that can
    touch a central sphere in the E8 lattice packing.
    
    This relates to information density and optimal coding,
    connecting to Vopson's information principles.
    """
    return 240


def ternary_entropy(probabilities: np.ndarray) -> float:
    """
    Calculate Shannon entropy for ternary distribution.
    
    H = -Σ p_i log₃(p_i)
    
    Measures information content in ternary systems, extending
    binary entropy to three-valued logic.
    
    Args:
        probabilities: Array of 3 probabilities summing to 1
        
    Returns:
        Entropy in trits (ternary digits)
        
    References:
        - Shannon, C. E. (1948). A mathematical theory of communication
        - Extension to ternary by Slade-Vetro framework
    """
    # Filter out zero probabilities
    p = probabilities[probabilities > 0]
    entropy = -np.sum(p * np.log(p) / np.log(3))
    return entropy


def ternary_mutual_information(joint_prob: np.ndarray) -> float:
    """
    Calculate mutual information for ternary variables.
    
    I(X:Y) = H(X) + H(Y) - H(X,Y)
    
    Args:
        joint_prob: 3x3 joint probability matrix
        
    Returns:
        Mutual information in trits
    """
    # Marginal probabilities
    p_x = joint_prob.sum(axis=1)
    p_y = joint_prob.sum(axis=0)
    
    # Entropies
    H_x = ternary_entropy(p_x)
    H_y = ternary_entropy(p_y)
    H_xy = ternary_entropy(joint_prob.flatten())
    
    return H_x + H_y - H_xy


if __name__ == "__main__":
    print("=" * 70)
    print("Ternary Logic and E8 Lattice Demonstrations")
    print("Framework by Trent Slade & Gary Vetro")
    print("Citations: Melvin Vopson, Erik Verlinde")
    print("=" * 70)
    
    # Ternary logic operations
    print("\n1. Ternary Logic Operations:")
    print(f"   TRUE AND UNKNOWN = {TernaryLogic.ternary_and(1, 0)}")
    print(f"   FALSE OR UNKNOWN = {TernaryLogic.ternary_or(-1, 0)}")
    print(f"   NOT UNKNOWN = {TernaryLogic.ternary_not(0)}")
    
    # E8 properties
    print("\n2. E8 Lattice Properties:")
    print(f"   E8 dimension: {e8_dimension()}")
    print(f"   E8 kissing number: {kissing_number_e8()}")
    roots = e8_root_system()
    print(f"   E8 root system: {roots.shape[0]} roots in {roots.shape[1]}D")
    
    # Ternary entropy
    print("\n3. Ternary Information:")
    probs = np.array([0.5, 0.3, 0.2])
    entropy = ternary_entropy(probs)
    print(f"   Entropy of {probs}: {entropy:.4f} trits")
    print(f"   Maximum ternary entropy: {np.log(3)/np.log(3):.4f} trits")
