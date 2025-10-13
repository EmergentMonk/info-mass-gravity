"""
Mass-Energy-Information Equivalence Module

Implements the Vopson mass-energy-information equivalence principle
and its connection to the Slade-Vetro informational mass framework.

CITATIONS:
- Trent Slade: Informational Mass Gravity Framework
- Gary Vetro: Informational Mass Gravity Framework  
- Melvin Vopson: Mass-energy-information equivalence principle
- Erik Verlinde: Entropic gravity and emergent spacetime

Provenance: Open Science Initiative
License: Open source for educational and research purposes
Ethics: These calculations explore theoretical relationships between
        information and physical properties. Results should be interpreted
        within established physics frameworks.
"""

import numpy as np
from typing import Tuple, Optional

# Physical constants
C = 299792458  # Speed of light (m/s)
H_BAR = 1.054571817e-34  # Reduced Planck constant (J·s)
K_B = 1.380649e-23  # Boltzmann constant (J/K)
VOPSON_CONSTANT = 3.19e-38  # Vopson's mass-per-bit constant (kg/bit)


def information_mass(bits: float) -> float:
    """
    Calculate the mass equivalent of information using Vopson's principle.
    
    m_info = N * m_bit
    
    where m_bit ≈ 3.19 × 10⁻³⁸ kg/bit (Vopson, 2019)
    
    Args:
        bits: Number of bits of information
        
    Returns:
        Mass in kilograms
        
    References:
        - Vopson, M. M. (2019). AIP Advances 9, 095206
        - Slade, T. & Vetro, G.: Informational mass framework
    """
    return bits * VOPSON_CONSTANT


def landauer_energy(bits: float, temperature: float = 300.0) -> float:
    """
    Calculate minimum energy to erase information (Landauer's principle).
    
    E = N * k_B * T * ln(2)
    
    Links information processing to thermodynamics, fundamental to
    Verlinde's entropic gravity.
    
    Args:
        bits: Number of bits erased
        temperature: Temperature in Kelvin (default 300K)
        
    Returns:
        Energy in Joules
        
    References:
        - Landauer, R. (1961). IBM J. Res. Dev.
        - Verlinde, E. (2011). Entropic forces
    """
    return bits * K_B * temperature * np.log(2)


def mass_from_energy(energy: float) -> float:
    """
    Calculate mass equivalent from energy using E = mc².
    
    Args:
        energy: Energy in Joules
        
    Returns:
        Mass in kilograms
    """
    return energy / (C ** 2)


def energy_from_mass(mass: float) -> float:
    """
    Calculate energy from mass using E = mc².
    
    Args:
        mass: Mass in kilograms
        
    Returns:
        Energy in Joules
    """
    return mass * C ** 2


def holographic_entropy_bound(area: float) -> float:
    """
    Calculate maximum entropy from holographic bound.
    
    S_max = k_B * A / (4 * l_p²)
    
    where l_p is Planck length. Fundamental to Verlinde's emergent gravity
    and the Slade-Vetro informational framework.
    
    Args:
        area: Area in square meters
        
    Returns:
        Maximum entropy in units of k_B
        
    References:
        - Bekenstein, J. (1973). Black hole entropy
        - Verlinde, E. (2011). Holographic principle in gravity
        - 't Hooft, G. (1993). Dimensional reduction
    """
    L_PLANCK = 1.616255e-35  # Planck length (m)
    return area / (4 * L_PLANCK ** 2)


def holographic_information_density(area: float) -> float:
    """
    Calculate information density from holographic principle.
    
    Connects area to maximum information content, key to understanding
    entropic gravity (Verlinde) and informational mass (Slade-Vetro).
    
    Args:
        area: Area in square meters
        
    Returns:
        Information density in bits per square meter
    """
    entropy_kb = holographic_entropy_bound(area)
    # Convert from natural units to bits
    bits = entropy_kb / np.log(2)
    return bits / area


def schwarzschild_information_entropy(mass: float) -> float:
    """
    Calculate the information/entropy of a Schwarzschild black hole.
    
    S = (k_B * c³ * A) / (4 * G * ℏ)
    
    Demonstrates the deep connection between gravity, information,
    and entropy central to Verlinde's theory.
    
    Args:
        mass: Black hole mass in kilograms
        
    Returns:
        Entropy in units of k_B
        
    References:
        - Bekenstein, J. & Hawking, S. (1974). Black hole thermodynamics
        - Verlinde, E. (2011). Entropic origin of gravity
    """
    G = 6.67430e-11  # Gravitational constant (m³/kg·s²)
    
    # Schwarzschild radius
    r_s = 2 * G * mass / (C ** 2)
    
    # Event horizon area
    area = 4 * np.pi * r_s ** 2
    
    # Bekenstein-Hawking entropy
    entropy = (K_B * C ** 3 * area) / (4 * G * H_BAR)
    
    return entropy / K_B  # Return in units of k_B


def information_density_to_mass_density(info_bits_per_m3: float) -> float:
    """
    Convert information density to mass density.
    
    Applies Vopson's principle to volumetric information density,
    connecting to the Slade-Vetro informational mass framework.
    
    Args:
        info_bits_per_m3: Information density in bits per cubic meter
        
    Returns:
        Mass density in kg/m³
    """
    return info_bits_per_m3 * VOPSON_CONSTANT


def emergent_force_from_entropy_gradient(
    entropy_gradient: float,
    temperature: float = 300.0
) -> float:
    """
    Calculate emergent force from entropy gradient (Verlinde).
    
    F = T * dS/dx
    
    Core equation of Verlinde's entropic gravity, showing how gravitational
    force emerges from information and thermodynamics.
    
    Args:
        entropy_gradient: Change in entropy per unit distance (1/m)
        temperature: Temperature in Kelvin
        
    Returns:
        Force in Newtons
        
    References:
        - Verlinde, E. (2011). On the origin of gravity
        - Slade, T. & Vetro, G.: Informational force framework
    """
    return temperature * K_B * entropy_gradient


def mass_defect_information(binding_energy: float) -> Tuple[float, float]:
    """
    Calculate mass defect and corresponding information content.
    
    Relates nuclear binding energy to information, demonstrating
    mass-energy-information equivalence (Vopson, Slade-Vetro).
    
    Args:
        binding_energy: Binding energy in Joules
        
    Returns:
        Tuple of (mass defect in kg, equivalent information in bits)
    """
    mass_defect = mass_from_energy(binding_energy)
    equivalent_bits = mass_defect / VOPSON_CONSTANT
    
    return mass_defect, equivalent_bits


if __name__ == "__main__":
    print("=" * 70)
    print("Mass-Energy-Information Equivalence Demonstrations")
    print("Framework by Trent Slade & Gary Vetro")
    print("Based on Melvin Vopson & Erik Verlinde's principles")
    print("=" * 70)
    
    # Example 1: Information mass
    print("\n1. Information Mass (Vopson):")
    bits = 1e20
    mass = information_mass(bits)
    print(f"   {bits:.2e} bits = {mass:.6e} kg")
    
    # Example 2: Landauer energy
    print("\n2. Landauer's Principle:")
    energy = landauer_energy(1000, 300)
    equiv_mass = mass_from_energy(energy)
    print(f"   Erasing 1000 bits at 300K: {energy:.6e} J")
    print(f"   Equivalent mass: {equiv_mass:.6e} kg")
    
    # Example 3: Black hole entropy
    print("\n3. Black Hole Information:")
    solar_mass = 1.989e30  # kg
    entropy = schwarzschild_information_entropy(solar_mass)
    print(f"   Solar mass black hole entropy: {entropy:.6e} k_B")
    
    # Example 4: Emergent force
    print("\n4. Verlinde's Emergent Force:")
    force = emergent_force_from_entropy_gradient(1e10, 300)
    print(f"   Force from entropy gradient: {force:.6e} N")
