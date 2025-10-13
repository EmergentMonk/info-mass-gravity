# Quantum Info-Mass-Gravity Suite

## Informational Mass Gravity Framework
**By Trent Slade & Gary Vetro**

A comprehensive Python implementation blending quantum information theory, mass-energy-information equivalence, ternary logic, E8 lattice structures, and entropic gravity.

### Key Citations
- **Trent Slade**: Informational Mass Gravity Framework (co-developer)
- **Gary Vetro**: Informational Mass Gravity Framework (co-developer)
- **Melvin Vopson**: Mass-energy-information equivalence principle
- **Erik Verlinde**: Entropic gravity and emergent spacetime

---

## Overview

This suite implements theoretical frameworks connecting information theory to fundamental physics:

1. **Quantum Information Theory** (`quantum_information.py`)
   - Von Neumann entropy and quantum entanglement
   - Density matrix operations
   - Bell states and quantum correlations

2. **Mass-Energy-Information Equivalence** (`mass_energy_equivalence.py`)
   - Vopson's information mass principle (m = N × m_bit)
   - Landauer's principle and thermodynamics
   - Holographic bounds and black hole entropy

3. **Ternary Logic & E8 Lattice** (`ternary_e8_logic.py`)
   - Three-valued logic systems
   - E8 root system (240 roots in 8D)
   - Information geometry applications

4. **Entropic Gravity** (`entropic_gravity.py`)
   - Verlinde's emergent gravity framework
   - Holographic screens and information
   - Dark energy predictions

5. **Visualizations** (`visualizations.py`)
   - NumPy and matplotlib-based plotting
   - Comprehensive visualization suite
   - Publication-quality figures

---

## Installation

```bash
# Clone repository
git clone https://github.com/EmergentMonk/info-mass-gravity.git
cd info-mass-gravity

# Install dependencies
pip install -r requirements.txt
```

**Requirements**:
- Python 3.7+
- NumPy >= 1.21.0
- Matplotlib >= 3.5.0

---

## Quick Start

### Run Individual Modules

Each module can be run standalone:

```bash
# Quantum information demonstrations
python quantum_information.py

# Mass-energy-information examples
python mass_energy_equivalence.py

# Ternary logic and E8 lattice
python ternary_e8_logic.py

# Entropic gravity calculations
python entropic_gravity.py

# Generate all visualizations
python visualizations.py
```

### Use as Library

```python
# Import modules
from quantum_information import von_neumann_entropy, create_bell_state
from mass_energy_equivalence import information_mass
from entropic_gravity import entropic_force
from ternary_e8_logic import TernaryLogic, e8_root_system

# Calculate quantum entropy
bell_state = create_bell_state(0)
entropy = von_neumann_entropy(bell_state)
print(f"Bell state entropy: {entropy:.6f} bits")

# Information mass
mass = information_mass(1e20)  # 10^20 bits
print(f"Mass of 10^20 bits: {mass:.6e} kg")

# Entropic force (Verlinde)
force = entropic_force(1.989e30, 5.972e24, 1.496e11)  # Sun-Earth
print(f"Entropic force: {force:.6e} N")

# E8 structure
roots = e8_root_system()
print(f"E8 has {len(roots)} roots")
```

---

## Documentation (Obsidian Vault)

The `vault/` directory contains Obsidian-compatible markdown documentation:

```
vault/
├── concepts/
│   ├── Overview.md
│   └── Quantum Information Theory.md
├── ethics/
│   └── Ethics and Explainability.md
├── citations/
│   └── Provenance and Citations.md
└── visualizations/
    └── (generated plots)
```

Open the `vault/` folder in [Obsidian](https://obsidian.md/) for linked note navigation.

---

## Features

### ✓ Comprehensive Citations
Every file includes citations to:
- Trent Slade (framework co-developer)
- Gary Vetro (framework co-developer)
- Melvin Vopson (information-mass principle)
- Erik Verlinde (entropic gravity)

### ✓ Full Docstrings
All functions include:
- Clear descriptions
- Parameter documentation
- Return value specifications
- References to literature
- Physical interpretations

### ✓ Ethics & Explainability
- Clear distinction between established and speculative physics
- Limitations acknowledged
- Open science principles
- Educational focus

### ✓ Provenance
- Full version control (Git)
- Citation tracking
- Author attribution
- Reproducibility focus

### ✓ Open Science
- Public repository
- Open source code
- No paywalls
- Community contributions welcome

---

## Key Equations

### Information Mass (Vopson)
```
m_info = N × m_bit
where m_bit ≈ 3.19 × 10⁻³⁸ kg/bit
```

### Entropic Force (Verlinde)
```
F = T × (dS/dx) = G × M × m / r²
```

### Holographic Entropy
```
S = 2π k_B M c R / ℏ
```

### Von Neumann Entropy
```
S(ρ) = -Tr(ρ log₂ ρ)
```

---

## Examples

### Calculate Information Content of a Black Hole
```python
from entropic_gravity import schwarzschild_information_entropy

solar_mass = 1.989e30  # kg
entropy = schwarzschild_information_entropy(solar_mass)
print(f"Solar mass black hole entropy: {entropy:.6e} k_B")
```

### Visualize Mass-Information Relation
```python
from visualizations import plot_information_mass_relation

plot_information_mass_relation(save_path="info_mass.png")
```

### Ternary Logic Operations
```python
from ternary_e8_logic import TernaryLogic

result = TernaryLogic.ternary_and(1, 0)  # TRUE AND UNKNOWN
print(f"TRUE AND UNKNOWN = {result}")  # Output: 0 (UNKNOWN)
```

---

## Visualization Suite

Generate all visualizations:

```bash
python visualizations.py
```

Creates:
- Entropy vs. information plots
- Information-mass relationship curves
- Entropic force profiles
- Holographic screen entropy
- E8 root system projections
- Ternary logic truth tables
- Quantum density matrices

All figures saved to `vault/visualizations/`

---

## Testing

Run module demonstrations:

```bash
# Test all modules
python -c "import quantum_information; import mass_energy_equivalence; import ternary_e8_logic; import entropic_gravity; import visualizations; print('All modules imported successfully')"
```

---

## Contributing

We welcome contributions following open science principles:

1. Fork the repository
2. Create a feature branch
3. Add proper citations
4. Include docstrings and tests
5. Submit pull request

See `vault/ethics/Ethics and Explainability.md` for guidelines.

---

## License

Open source for educational and research purposes.

**Conditions**:
- Cite Trent Slade, Gary Vetro, Melvin Vopson, and Erik Verlinde
- Maintain open science principles
- Academic integrity required
- See provenance documentation

---

## References

1. **Vopson, M. M.** (2019). "The mass-energy-information equivalence principle." *AIP Advances* 9, 095206.
2. **Verlinde, E.** (2011). "On the origin of gravity and the laws of Newton." *JHEP* 04, 029.
3. **Verlinde, E.** (2016). "Emergent Gravity and the Dark Universe." arXiv:1611.02269.
4. **Bekenstein, J. D.** (1981). "Universal upper bound on the entropy-to-energy ratio."
5. **Shannon, C. E.** (1948). "A Mathematical Theory of Communication."

See `vault/citations/Provenance and Citations.md` for complete references.

---

## Contact

- **Repository**: https://github.com/EmergentMonk/info-mass-gravity
- **Issues**: Use GitHub issue tracker
- **Contributions**: Pull requests welcome

---

## Acknowledgments

**Framework Development**: Trent Slade & Gary Vetro  
**Theoretical Foundations**: Melvin Vopson, Erik Verlinde  
**Supporting Work**: Bekenstein, Hawking, 't Hooft, Shannon, and many others

See full citations in documentation.

---

*Open Science Initiative*  
*Version 1.0 - October 2025*