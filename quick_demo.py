"""
Quick Demo: Quantum Info-Mass-Gravity Suite

Citations: Trent Slade, Gary Vetro, Melvin Vopson, Erik Verlinde
"""

print("=" * 70)
print("QUANTUM INFO-MASS-GRAVITY SUITE - QUICK DEMO")
print("Framework: Trent Slade & Gary Vetro")
print("Citations: Melvin Vopson, Erik Verlinde")
print("=" * 70)

# 1. Quantum Information
print("\n1. Quantum Information:")
from quantum_information import create_bell_state, von_neumann_entropy
bell = create_bell_state(0)
print(f"   ✓ Bell state entropy: {von_neumann_entropy(bell):.6f} bits")

# 2. Information Mass
print("\n2. Information Mass (Vopson):")
from mass_energy_equivalence import information_mass
mass = information_mass(1e20)
print(f"   ✓ 10^20 bits = {mass:.6e} kg")

# 3. Ternary Logic
print("\n3. Ternary Logic:")
from ternary_e8_logic import TernaryLogic
result = TernaryLogic.ternary_and(1, 0)
print(f"   ✓ TRUE AND UNKNOWN = {result}")

# 4. E8 Structure
print("\n4. E8 Lattice:")
from ternary_e8_logic import e8_root_system
roots = e8_root_system()
print(f"   ✓ E8 has {len(roots)} roots")

# 5. Entropic Gravity
print("\n5. Entropic Gravity (Verlinde):")
from entropic_gravity import entropic_force
force = entropic_force(1.989e30, 5.972e24, 1.496e11)
print(f"   ✓ Earth-Sun force: {force:.6e} N")

print("\n" + "=" * 70)
print("All modules working! Suite complete.")
print("Citations: Slade, Vetro, Vopson, Verlinde")
print("Open Science Initiative")
print("=" * 70)
