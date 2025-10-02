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


# Import student function
import importlib.util

spec = importlib.util.spec_from_file_location("assignment", "assignment/assignment.py")
assignment_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assignment_module)

compute_closeness_centrality = assignment_module.compute_closeness_centrality

print("=" * 60)
print("Test 2: Closeness Centrality")
print("=" * 60)

# %% Test Setup
# Create a simple star graph: node 0 is center, connected to all others
g_star = igraph.Graph.Star(5, mode="undirected")
print(f"\n[Setup] Created star graph with 5 nodes")
print(f"  Node 0 (center) is connected to all others")
print(f"  Expected: Node 0 has closeness = 1.0 (distance 1 to all)")

# %% Test execution
closeness_values = compute_closeness_centrality(g_star)
print(f"\n[Result] Computed closeness values: {closeness_values}")

# %% Test 1: Function returns correct type
print("\n[Test 2.1] Checking return type")
assert isinstance(
    closeness_values, (list, np.ndarray)
), f"compute_closeness_centrality should return a list or array, got {type(closeness_values)}"
print("✓ Returns list or array")

# %% Test 2: Correct number of values
print("\n[Test 2.2] Checking number of values")
assert (
    len(closeness_values) == 5
), f"Expected 5 closeness values for 5 nodes, got {len(closeness_values)}"
print("✓ Returns correct number of values")

# %% Test 3: Center node has highest closeness
print("\n[Test 2.3] Checking center node has highest closeness")
max_closeness_node = np.argmax(closeness_values)
assert (
    max_closeness_node == 0
), f"Center node (0) should have highest closeness, but node {max_closeness_node} does"
print(f"✓ Node {max_closeness_node} has highest closeness")

# %% Test 4: Center node closeness value
print("\n[Test 2.4] Checking center node closeness value")
assert np.isclose(
    closeness_values[0], 1.0, rtol=1e-5
), f"Center node closeness should be 1.0, got {closeness_values[0]}"
print(f"✓ Center node has closeness {closeness_values[0]:.4f}")

# %% Test 5: All values are positive
print("\n[Test 2.5] Checking all values are positive")
for i, val in enumerate(closeness_values):
    assert val > 0, f"Closeness for node {i} should be positive, got {val}"
print("✓ All closeness values are positive")

# %% Summary
print("\n" + "=" * 60)
print("All tests passed for Task 2! ✓")
print("=" * 60)
