# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "numpy==2.2.6",
#     "python-igraph==0.11.9",
# ]
# ///

# %% Import
import numpy as np
import sys
import os
import igraph

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import student function
import importlib.util

spec = importlib.util.spec_from_file_location(
    "for_instructor", "for_instructor/assignment.py"
)
assignment_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assignment_module)

compute_eccentricity_centrality = assignment_module.compute_eccentricity_centrality

print("=" * 60)
print("Test 4: Eccentricity Centrality")
print("=" * 60)

# %% Test Setup
# Create a simple star graph: node 0 is center, connected to all others
g_star = igraph.Graph.Star(5, mode="undirected")
print(f"\n[Setup] Created star graph with 5 nodes")
print(f"  Node 0 (center) has max distance 1 to any node")
print(f"  Leaf nodes have max distance 2 to any node")
print(f"  Expected: Node 0 has eccentricity 1, leaves have 2")

# %% Test execution
eccentricity_values = compute_eccentricity_centrality(g_star)
print(f"\n[Result] Computed eccentricity values: {eccentricity_values}")

# %% Test 1: Function returns correct type
print("\n[Test 4.1] Checking return type")
assert isinstance(
    eccentricity_values, (list, np.ndarray)
), f"compute_eccentricity_centrality should return a list or array, got {type(eccentricity_values)}"
print("✓ Returns list or array")

# %% Test 2: Correct number of values
print("\n[Test 4.2] Checking number of values")
assert (
    len(eccentricity_values) == 5
), f"Expected 5 eccentricity values for 5 nodes, got {len(eccentricity_values)}"
print("✓ Returns correct number of values")

# %% Test 3: Center node has lowest eccentricity
print("\n[Test 4.3] Checking center node has lowest eccentricity")
min_eccentricity_node = np.argmin(eccentricity_values)
assert (
    min_eccentricity_node == 0
), f"Center node (0) should have lowest eccentricity, but node {min_eccentricity_node} does"
print(f"✓ Node {min_eccentricity_node} has lowest eccentricity")

# %% Test 4: Center node eccentricity value
print("\n[Test 4.4] Checking center node eccentricity value")
assert (
    eccentricity_values[0] == 1
), f"Center node eccentricity should be 1, got {eccentricity_values[0]}"
print(f"✓ Center node has eccentricity {eccentricity_values[0]}")

# %% Test 5: Leaf nodes have eccentricity 2
print("\n[Test 4.5] Checking leaf nodes have eccentricity 2")
for i in range(1, 5):
    assert (
        eccentricity_values[i] == 2
    ), f"Leaf node {i} should have eccentricity 2, got {eccentricity_values[i]}"
print("✓ All leaf nodes have eccentricity 2")

# %% Summary
print("\n" + "=" * 60)
print("All tests passed for Task 4! ✓")
print("=" * 60)
