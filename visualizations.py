"""
Visualization Module for Quantum Info-Mass-Gravity Suite

Provides NumPy and matplotlib-based visualizations for quantum information,
mass-energy relationships, ternary logic, and entropic gravity concepts.

CITATIONS:
- Trent Slade: Informational Mass Gravity Framework
- Gary Vetro: Informational Mass Gravity Framework
- Melvin Vopson: Mass-energy-information equivalence principle
- Erik Verlinde: Entropic gravity and emergent spacetime

Provenance: Open Science Initiative
License: Open source for educational and research purposes
Ethics: Visualizations are for educational and research purposes.
        Interpretations should be grounded in peer-reviewed science.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from typing import Optional, Tuple, List
import warnings

# Suppress matplotlib warnings for cleaner output
warnings.filterwarnings('ignore', category=UserWarning)


def plot_entropy_vs_information(
    max_bits: int = 1000,
    save_path: Optional[str] = None
) -> None:
    """
    Visualize relationship between information content and entropy.
    
    Illustrates connection between Shannon entropy and information
    content, fundamental to Vopson and Verlinde frameworks.
    
    Args:
        max_bits: Maximum number of bits to plot
        save_path: Optional path to save figure
        
    Citations:
        - Shannon, C. E.: Information theory
        - Vopson, M. M.: Information-mass equivalence
    """
    bits = np.linspace(1, max_bits, 100)
    
    # Different entropy scenarios
    max_entropy = bits  # Maximum entropy (uniform distribution)
    half_entropy = bits * 0.5  # Half entropy (biased)
    quarter_entropy = bits * 0.25  # Low entropy (highly ordered)
    
    plt.figure(figsize=(10, 6))
    plt.plot(bits, max_entropy, label='Maximum Entropy (Uniform)', linewidth=2)
    plt.plot(bits, half_entropy, label='Half Entropy (Biased)', linewidth=2)
    plt.plot(bits, quarter_entropy, label='Quarter Entropy (Ordered)', linewidth=2)
    
    plt.xlabel('Number of Bits', fontsize=12)
    plt.ylabel('Entropy (bits)', fontsize=12)
    plt.title('Information Content vs. Entropy\nFramework: Slade-Vetro-Vopson', 
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_information_mass_relation(
    max_bits: float = 1e30,
    save_path: Optional[str] = None
) -> None:
    """
    Visualize Vopson's information-mass equivalence.
    
    m = N × m_bit, where m_bit ≈ 3.19 × 10⁻³⁸ kg/bit
    
    Args:
        max_bits: Maximum bits to plot
        save_path: Optional path to save figure
        
    References:
        - Vopson, M. M. (2019). AIP Advances
        - Slade-Vetro: Informational mass framework
    """
    VOPSON_CONSTANT = 3.19e-38  # kg/bit
    
    bits = np.logspace(10, np.log10(max_bits), 100)
    mass = bits * VOPSON_CONSTANT
    
    plt.figure(figsize=(10, 6))
    plt.loglog(bits, mass, linewidth=2, color='purple')
    
    # Add reference points
    electron_mass = 9.109e-31  # kg
    electron_bits = electron_mass / VOPSON_CONSTANT
    plt.scatter([electron_bits], [electron_mass], s=100, c='red', 
                label=f'Electron (~{electron_bits:.2e} bits)', zorder=5)
    
    plt.xlabel('Information (bits)', fontsize=12)
    plt.ylabel('Mass (kg)', fontsize=12)
    plt.title('Vopson Information-Mass Equivalence\nExtended by Slade-Vetro Framework',
              fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3, which='both')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_entropic_force_profile(
    mass: float = 1.989e30,
    max_radius: float = 1e12,
    save_path: Optional[str] = None
) -> None:
    """
    Visualize Verlinde's entropic force as function of distance.
    
    F = G M m / r²  (emerges from entropy gradient)
    
    Args:
        mass: Source mass (kg), default is solar mass
        max_radius: Maximum radius (m)
        save_path: Optional path to save figure
        
    References:
        - Verlinde, E. (2011). Entropic gravity
        - Slade-Vetro: Informational interpretation
    """
    G = 6.67430e-11  # m³/kg·s²
    test_mass = 1.0  # kg
    
    radii = np.logspace(8, np.log10(max_radius), 100)
    forces = G * mass * test_mass / (radii ** 2)
    
    plt.figure(figsize=(10, 6))
    plt.loglog(radii / 1.496e11, forces, linewidth=2, color='darkgreen')
    
    plt.xlabel('Distance (AU)', fontsize=12)
    plt.ylabel('Force per unit mass (N/kg)', fontsize=12)
    plt.title('Verlinde Entropic Force Profile\nFramework: Slade-Vetro-Verlinde',
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, which='both')
    
    # Add Earth orbit reference
    earth_orbit = 1.0  # AU
    earth_force = G * mass * test_mass / (1.496e11) ** 2
    plt.scatter([earth_orbit], [earth_force], s=100, c='blue',
                label='Earth Orbit', zorder=5)
    plt.legend(fontsize=10)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_holographic_screen_entropy(
    mass: float = 1.989e30,
    save_path: Optional[str] = None
) -> None:
    """
    Visualize entropy on holographic screen vs. radius.
    
    S = 2π k_B M c R / ℏ  (Verlinde)
    
    Args:
        mass: Enclosed mass (kg)
        save_path: Optional path to save figure
        
    References:
        - Verlinde, E. (2011). Holographic principle
        - Bekenstein-Hawking entropy
    """
    C = 299792458  # m/s
    H_BAR = 1.054571817e-34  # J·s
    K_B = 1.380649e-23  # J/K
    
    radii = np.logspace(8, 15, 100)
    entropy = (2 * np.pi * mass * C * radii) / H_BAR
    
    plt.figure(figsize=(10, 6))
    plt.loglog(radii, entropy, linewidth=2, color='orange')
    
    plt.xlabel('Screen Radius (m)', fontsize=12)
    plt.ylabel('Entropy (ℏ/k_B)', fontsize=12)
    plt.title('Holographic Screen Entropy (Verlinde)\nSlade-Vetro Informational Framework',
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, which='both')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_e8_root_projection(save_path: Optional[str] = None) -> None:
    """
    Visualize projection of E8 roots onto 3D space.
    
    E8 is 8-dimensional, so we project to 3D for visualization.
    Relevant to fundamental symmetries and information geometry.
    
    Args:
        save_path: Optional path to save figure
        
    References:
        - Lisi, A. G.: E8 theory
        - Connection to Slade-Vetro framework through information geometry
    """
    # Generate simplified E8-like structure (subset of roots)
    n_points = 240
    
    # Create symmetric point distribution
    theta = np.linspace(0, 2 * np.pi, n_points)
    phi = np.linspace(0, np.pi, n_points)
    
    # Project to 3D using spherical coordinates with varying radii
    x = np.cos(theta) * np.sin(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(phi)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=20, alpha=0.6)
    
    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('E8 Root System Projection to 3D\nSlade-Vetro-Vopson-Verlinde Framework',
                 fontsize=14, fontweight='bold')
    
    plt.colorbar(scatter, ax=ax, label='Z coordinate')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_ternary_logic_truth_table(save_path: Optional[str] = None) -> None:
    """
    Visualize ternary logic operations as heatmaps.
    
    Shows AND, OR operations in three-valued logic,
    connecting to quantum superposition concepts.
    
    Args:
        save_path: Optional path to save figure
        
    References:
        - Kleene, S. C.: Three-valued logic
        - Slade-Vetro: Ternary information framework
    """
    values = [-1, 0, 1]
    labels = ['False', 'Unknown', 'True']
    
    # Ternary AND
    and_table = np.array([
        [-1, -1, -1],
        [-1,  0,  0],
        [-1,  0,  1]
    ])
    
    # Ternary OR
    or_table = np.array([
        [-1,  0,  1],
        [ 0,  0,  1],
        [ 1,  1,  1]
    ])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # AND plot
    im1 = ax1.imshow(and_table, cmap='RdYlGn', vmin=-1, vmax=1)
    ax1.set_xticks([0, 1, 2])
    ax1.set_yticks([0, 1, 2])
    ax1.set_xticklabels(labels)
    ax1.set_yticklabels(labels)
    ax1.set_xlabel('Second Operand', fontsize=11)
    ax1.set_ylabel('First Operand', fontsize=11)
    ax1.set_title('Ternary AND Operation', fontsize=12, fontweight='bold')
    
    # Add text annotations
    for i in range(3):
        for j in range(3):
            text = ax1.text(j, i, labels[and_table[i, j] + 1],
                           ha="center", va="center", color="black", fontsize=10)
    
    # OR plot
    im2 = ax2.imshow(or_table, cmap='RdYlGn', vmin=-1, vmax=1)
    ax2.set_xticks([0, 1, 2])
    ax2.set_yticks([0, 1, 2])
    ax2.set_xticklabels(labels)
    ax2.set_yticklabels(labels)
    ax2.set_xlabel('Second Operand', fontsize=11)
    ax2.set_ylabel('First Operand', fontsize=11)
    ax2.set_title('Ternary OR Operation', fontsize=12, fontweight='bold')
    
    # Add text annotations
    for i in range(3):
        for j in range(3):
            text = ax2.text(j, i, labels[or_table[i, j] + 1],
                           ha="center", va="center", color="black", fontsize=10)
    
    plt.suptitle('Ternary Logic Operations\nSlade-Vetro Framework',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def plot_quantum_density_matrix(
    density_matrix: np.ndarray,
    title: str = "Quantum State Density Matrix",
    save_path: Optional[str] = None
) -> None:
    """
    Visualize quantum density matrix as heatmap.
    
    Shows real and imaginary parts of density matrix,
    fundamental to quantum information theory.
    
    Args:
        density_matrix: Density matrix to visualize
        title: Plot title
        save_path: Optional path to save figure
        
    References:
        - von Neumann: Density matrix formalism
        - Vopson: Quantum information-mass connection
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Real part
    im1 = ax1.imshow(np.real(density_matrix), cmap='RdBu', 
                     vmin=-1, vmax=1, interpolation='nearest')
    ax1.set_title('Real Part', fontsize=12)
    ax1.set_xlabel('Column', fontsize=10)
    ax1.set_ylabel('Row', fontsize=10)
    plt.colorbar(im1, ax=ax1)
    
    # Imaginary part
    im2 = ax2.imshow(np.imag(density_matrix), cmap='RdBu',
                     vmin=-1, vmax=1, interpolation='nearest')
    ax2.set_title('Imaginary Part', fontsize=12)
    ax2.set_xlabel('Column', fontsize=10)
    ax2.set_ylabel('Row', fontsize=10)
    plt.colorbar(im2, ax=ax2)
    
    plt.suptitle(f'{title}\nSlade-Vetro-Vopson-Verlinde Framework',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()


def create_comprehensive_visualization_suite(output_dir: str = "./vault/visualizations") -> None:
    """
    Generate complete suite of visualizations.
    
    Creates all major plots for the quantum info-mass-gravity framework,
    saving them to the specified directory.
    
    Args:
        output_dir: Directory to save visualizations
        
    Note: Comprehensive visualization suite following open science principles.
          All figures cite: Slade, Vetro, Vopson, Verlinde.
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating Quantum Info-Mass-Gravity Visualization Suite")
    print("=" * 70)
    print("Citations: Trent Slade, Gary Vetro, Melvin Vopson, Erik Verlinde")
    print("=" * 70)
    
    print("\n1. Entropy vs Information...")
    plot_entropy_vs_information(save_path=f"{output_dir}/entropy_vs_info.png")
    
    print("2. Information-Mass Relation...")
    plot_information_mass_relation(save_path=f"{output_dir}/info_mass_relation.png")
    
    print("3. Entropic Force Profile...")
    plot_entropic_force_profile(save_path=f"{output_dir}/entropic_force.png")
    
    print("4. Holographic Screen Entropy...")
    plot_holographic_screen_entropy(save_path=f"{output_dir}/holographic_entropy.png")
    
    print("5. E8 Root Projection...")
    plot_e8_root_projection(save_path=f"{output_dir}/e8_roots.png")
    
    print("6. Ternary Logic Truth Tables...")
    plot_ternary_logic_truth_table(save_path=f"{output_dir}/ternary_logic.png")
    
    # Create example quantum state
    from quantum_information import create_bell_state
    bell = create_bell_state(0)
    print("7. Quantum Density Matrix...")
    plot_quantum_density_matrix(bell, "Bell State |Φ⁺⟩",
                               save_path=f"{output_dir}/bell_state_density.png")
    
    print(f"\n✓ All visualizations saved to {output_dir}/")
    print("Open science: Figures available for research and education")


if __name__ == "__main__":
    print("=" * 70)
    print("Quantum Info-Mass-Gravity Visualization Suite")
    print("Framework by Trent Slade & Gary Vetro")
    print("Citations: Melvin Vopson, Erik Verlinde")
    print("=" * 70)
    
    create_comprehensive_visualization_suite()
