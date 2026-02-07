# Day 2 – Quantum Probability Simulation
# Concept: Measurement probability = |amplitude|^2

import random

# Quantum state amplitudes
alpha = 0.6   # amplitude of |0>
beta = 0.8    # amplitude of |1>

# Sanity check (normalization)
assert round(alpha**2 + beta**2, 5) == 1.0

shots = 10000
results = {"0": 0, "1": 0}

for _ in range(shots):
    r = random.random()
    if r < alpha**2:
        results["0"] += 1
    else:
        results["1"] += 1

print("Measurement results after", shots, "shots:")
print("|0>:", results["0"] / shots)
print("|1>:", results["1"] / shots)
