# Usage Guide: Quantum Info-Mass-Gravity Suite

**Framework by**: Trent Slade & Gary Vetro  
**Citations**: Melvin Vopson, Erik Verlinde

---

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Module Overview](#module-overview)
4. [Examples](#examples)
5. [Visualization](#visualization)
6. [Obsidian Vault](#obsidian-vault)
7. [Advanced Usage](#advanced-usage)
8. [Troubleshooting](#troubleshooting)

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone Repository
```bash
git clone https://github.com/EmergentMonk/info-mass-gravity.git
cd info-mass-gravity
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- NumPy (≥1.21.0)
- Matplotlib (≥3.5.0)

### Step 3: Verify Installation
```bash
python -c "import quantum_information; print('✓ Installation successful')"
```

---

## Quick Start

### Run Demonstrations
Each module has built-in demonstrations:

```bash
# Quantum information examples
python quantum_information.py

# Mass-energy-information equivalence
python mass_energy_equivalence.py

# Ternary logic and E8 lattice
python ternary_e8_logic.py

# Entropic gravity
python entropic_gravity.py

# Quantum error correction tests
python qec_test.py

# Complete example suite
python example_suite.py

# Generate all visualizations
python visualizations.py
```

### Basic Python Usage
```python
# Import modules
from quantum_information import von_neumann_entropy, create_bell_state
from mass_energy_equivalence import information_mass
from entropic_gravity import entropic_force

# Calculate quantum entropy
bell_state = create_bell_state(0)
entropy = von_neumann_entropy(bell_state)
print(f"Bell state entropy: {entropy:.6f} bits")

# Calculate information mass
mass = information_mass(1e20)  # 10^20 bits
print(f"Mass: {mass:.6e} kg")

# Calculate entropic force
M_sun = 1.989e30  # kg
M_earth = 5.972e24  # kg
R_au = 1.496e11  # m
force = entropic_force(M_sun, M_earth, R_au)
print(f"Force: {force:.6e} N")
```

---

## Module Overview

### 1. `quantum_information.py`
Quantum information theory fundamentals.

**Key Functions**:
- `von_neumann_entropy(density_matrix)`: Quantum entropy
- `create_bell_state(which)`: Generate Bell states
- `entanglement_entropy(rho_AB, dim_A, dim_B)`: Entanglement measure
- `quantum_fidelity(rho, sigma)`: State distinguishability
- `partial_trace(rho, dim_A, dim_B, trace_over)`: Reduced density matrix

**Example**:
```python
from quantum_information import *

# Create maximally entangled state
bell = create_bell_state(0)  # |Φ⁺⟩

# Calculate entanglement
S_ent = entanglement_entropy(bell, 2, 2)
print(f"Entanglement: {S_ent:.6f} bits")  # Output: 1.000000
```

### 2. `mass_energy_equivalence.py`
Vopson's information-mass equivalence.

**Key Functions**:
- `information_mass(bits)`: Mass from information
- `landauer_energy(bits, temperature)`: Erasure energy
- `schwarzschild_information_entropy(mass)`: Black hole entropy
- `holographic_entropy_bound(area)`: Maximum entropy
- `emergent_force_from_entropy_gradient(gradient, temp)`: Force from entropy

**Example**:
```python
from mass_energy_equivalence import *

# Information mass
bits = 1e30
mass = information_mass(bits)
print(f"{bits:.2e} bits = {mass:.6e} kg")

# Landauer's principle
energy = landauer_energy(1000, 300)  # 1000 bits at 300K
print(f"Erasure energy: {energy:.6e} J")
```

### 3. `ternary_e8_logic.py`
Ternary logic and E8 lattice structures.

**Key Functions**:
- `TernaryLogic.ternary_and(a, b)`: Ternary AND
- `TernaryLogic.ternary_or(a, b)`: Ternary OR
- `TernaryLogic.ternary_not(a)`: Ternary NOT
- `e8_root_system()`: Generate E8 roots
- `ternary_entropy(probabilities)`: Ternary entropy
- `kissing_number_e8()`: E8 kissing number

**Example**:
```python
from ternary_e8_logic import *
import numpy as np

# Ternary logic
result = TernaryLogic.ternary_and(1, 0)  # TRUE AND UNKNOWN
print(f"Result: {result}")  # Output: 0 (UNKNOWN)

# E8 roots
roots = e8_root_system()
print(f"E8 has {len(roots)} roots")  # Output: 240

# Ternary entropy
probs = np.array([0.5, 0.3, 0.2])
H = ternary_entropy(probs)
print(f"Entropy: {H:.4f} trits")
```

### 4. `entropic_gravity.py`
Verlinde's entropic gravity framework.

**Key Functions**:
- `entropic_force(mass_source, mass_test, distance)`: Gravitational force
- `holographic_screen_entropy(radius, mass)`: Screen entropy
- `information_bits_on_screen(radius, mass)`: Information content
- `bekenstein_bound(energy, radius)`: Maximum information
- `dark_energy_entropic(hubble_constant)`: Dark energy density

**Example**:
```python
from entropic_gravity import *

# Earth-Sun force
M_sun = 1.989e30  # kg
M_earth = 5.972e24  # kg
R_au = 1.496e11  # m

force = entropic_force(M_sun, M_earth, R_au)
print(f"Entropic force: {force:.6e} N")

# Information on screen
bits = information_bits_on_screen(R_au, M_sun)
print(f"Information: {bits:.6e} bits")
```

### 5. `qec_test.py`
Quantum error correction with trinary repetition codes.

**Key Functions**:
- `encode_qutrit(data)`: Encode single trit as repetition code
- `introduce_error(codeword, pos, error_trit)`: Simulate trit-flip error
- `decode_qutrit(codeword)`: Decode using majority vote
- `test_qec_no_error()`: Test without errors
- `test_qec_with_error()`: Test with single-error correction
- `run_qec_demonstration()`: Comprehensive QEC demo

**Example**:
```python
from qec_test import *

# Encode trit
data = 1
encoded = encode_qutrit(data)
print(f"Encoded: {encoded}")  # Output: [1, 1, 1]

# Introduce error
corrupted = introduce_error(encoded, 0, 2)
print(f"Corrupted: {corrupted}")  # Output: [2, 1, 1]

# Correct error
decoded = decode_qutrit(corrupted)
print(f"Decoded: {decoded}")  # Output: 1 (corrected!)
```

### 6. `visualizations.py`
Comprehensive visualization suite.

**Key Functions**:
- `plot_entropy_vs_information()`: Entropy-information relation
- `plot_information_mass_relation()`: Vopson's principle
- `plot_entropic_force_profile()`: Force vs distance
- `plot_holographic_screen_entropy()`: Entropy vs radius
- `plot_e8_root_projection()`: E8 structure
- `plot_ternary_logic_truth_table()`: Ternary operations
- `plot_quantum_density_matrix()`: Quantum states
- `create_comprehensive_visualization_suite()`: Generate all

**Example**:
```python
from visualizations import *

# Generate single plot
plot_information_mass_relation(save_path="info_mass.png")

# Generate all visualizations
create_comprehensive_visualization_suite(output_dir="./figures")
```

---

## Examples

### Example 1: Quantum State Analysis
```python
from quantum_information import *
import numpy as np

# Create pure state
psi = np.array([1, 0, 0, 1]) / np.sqrt(2)  # |00⟩ + |11⟩
rho = np.outer(psi, psi.conj())

# Calculate entropy
S = von_neumann_entropy(rho)
print(f"Pure state entropy: {S:.6f} bits")  # Should be 0

# Calculate entanglement
S_ent = entanglement_entropy(rho, 2, 2)
print(f"Entanglement entropy: {S_ent:.6f} bits")  # Should be 1
```

### Example 2: Information-Mass Chain
```python
from quantum_information import von_neumann_entropy, create_bell_state
from mass_energy_equivalence import information_mass
from entropic_gravity import entropic_force

# 1. Quantum information
bell = create_bell_state(0)
entropy_bits = entanglement_entropy(bell, 2, 2)

# 2. Information → Mass
mass = information_mass(entropy_bits)

# 3. Mass → Gravitational force
force = entropic_force(mass, 1.0, 1.0)  # 1kg at 1m

print(f"Entropy: {entropy_bits:.6f} bits")
print(f"Mass: {mass:.6e} kg")
print(f"Force: {force:.6e} N")
```

### Example 3: Black Hole Analysis
```python
from mass_energy_equivalence import schwarzschild_information_entropy
from entropic_gravity import schwarzschild_radius
import numpy as np

# Solar mass black hole
M_sun = 1.989e30  # kg

# Schwarzschild radius
r_s = schwarzschild_radius(M_sun)
print(f"Schwarzschild radius: {r_s:.2f} m")

# Information content
entropy = schwarzschild_information_entropy(M_sun)
bits = entropy / np.log(2)
print(f"Information: {bits:.6e} bits")

# Information mass (Vopson)
from mass_energy_equivalence import information_mass
info_mass = information_mass(bits)
print(f"Information mass: {info_mass:.6e} kg")
```

### Example 4: Dark Energy Prediction
```python
from entropic_gravity import dark_energy_entropic

# Current Hubble constant
H0 = 70  # km/s/Mpc

# Verlinde's prediction
rho_de = dark_energy_entropic(H0)
print(f"Dark energy density: {rho_de:.6e} J/m³")

# Compare with observations (~6 × 10⁻¹⁰ J/m³)
observed = 6e-10
ratio = rho_de / observed
print(f"Prediction/Observation ratio: {ratio:.2f}")
```

---

## Visualization

### Generate All Plots
```python
from visualizations import create_comprehensive_visualization_suite

# Generate in default directory
create_comprehensive_visualization_suite()

# Generate in custom directory
create_comprehensive_visualization_suite(output_dir="./my_figures")
```

### Custom Plots
```python
from visualizations import *

# Entropy vs information
plot_entropy_vs_information(
    max_bits=1000,
    save_path="entropy.png"
)

# Information-mass relation
plot_information_mass_relation(
    max_bits=1e30,
    save_path="mass.png"
)

# Entropic force profile
plot_entropic_force_profile(
    mass=1.989e30,  # Solar mass
    max_radius=1e12,
    save_path="force.png"
)

# Quantum density matrix
from quantum_information import create_bell_state
bell = create_bell_state(0)
plot_quantum_density_matrix(
    bell,
    title="Bell State",
    save_path="bell.png"
)
```

---

## Obsidian Vault

### Opening the Vault
1. Install [Obsidian](https://obsidian.md/)
2. Open Obsidian
3. Select "Open folder as vault"
4. Navigate to `vault/` directory
5. Explore linked documentation

### Vault Structure
```
vault/
├── concepts/          # Theoretical foundations
│   ├── Overview.md
│   ├── Quantum Information Theory.md
│   ├── E8 Lattice.md
│   └── Entropic Gravity.md
├── ethics/            # Ethics and explainability
│   └── Ethics and Explainability.md
├── citations/         # Provenance and citations
│   └── Provenance and Citations.md
└── visualizations/    # Generated plots
    └── (PNG files)
```

### Navigation
- Click `[[Links]]` to navigate between notes
- Use graph view to see connections
- Search with Ctrl+Shift+F

---

## Advanced Usage

### Custom Quantum States
```python
import numpy as np
from quantum_information import von_neumann_entropy

# Create custom density matrix
dim = 4
rho = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
rho = rho @ rho.conj().T  # Make positive semidefinite
rho = rho / np.trace(rho)  # Normalize

# Calculate entropy
S = von_neumann_entropy(rho)
print(f"Entropy: {S:.6f} bits")
```

### Information Acceleration
```python
from entropic_gravity import information_acceleration

# System with information content
mass = 1e20  # kg
distance = 1e6  # m
info_bits = 1e30  # bits

# Acceleration including information
a = information_acceleration(mass, distance, info_bits)
print(f"Acceleration: {a:.6e} m/s²")
```

### Ternary Information Processing
```python
from ternary_e8_logic import *
import numpy as np

# Ternary mutual information
joint_prob = np.array([
    [0.2, 0.1, 0.05],
    [0.15, 0.2, 0.1],
    [0.05, 0.1, 0.05]
])

I = ternary_mutual_information(joint_prob)
print(f"Mutual information: {I:.4f} trits")
```

---

## Troubleshooting

### Import Errors
```bash
# If modules not found
export PYTHONPATH="${PYTHONPATH}:/path/to/info-mass-gravity"

# Or use absolute imports
import sys
sys.path.append('/path/to/info-mass-gravity')
```

### NumPy/Matplotlib Issues
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or install specific versions
pip install numpy==1.21.0 matplotlib==3.5.0
```

### Visualization Not Displaying
```python
# Use non-interactive backend
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Or explicitly show
plt.show()
```

### Numerical Warnings
Some calculations involve very small/large numbers. This is expected:
```python
import warnings
warnings.filterwarnings('ignore')
```

---

## Citations

When using this suite, please cite:

**Framework**:
```
Slade, T. & Vetro, G. (2025). Quantum Info-Mass-Gravity Suite.
GitHub: https://github.com/EmergentMonk/info-mass-gravity
```

**Theoretical Foundations**:
- **Vopson, M. M.** (2019). AIP Advances 9, 095206.
- **Verlinde, E.** (2011). JHEP 04, 029.
- **Verlinde, E.** (2016). arXiv:1611.02269.

See `vault/citations/Provenance and Citations.md` for complete references.

---

## Support

- **Repository**: https://github.com/EmergentMonk/info-mass-gravity
- **Issues**: GitHub issue tracker
- **Documentation**: `vault/` directory (Obsidian)

---

*Framework: Trent Slade & Gary Vetro*  
*Citations: Melvin Vopson, Erik Verlinde*  
*Open Science Initiative*
