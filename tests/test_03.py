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

compute_betweenness_centrality = assignment_module.compute_betweenness_centrality

print("=" * 60)
print("Test 3: Betweenness Centrality")
print("=" * 60)

# %% Test Setup
# Create a simple star graph: node 0 is center, connected to all others
g_star = igraph.Graph.Star(5, mode="undirected")
print(f"\n[Setup] Created star graph with 5 nodes")
print(f"  Node 0 (center) is on all shortest paths between leaf nodes")
print(f"  Expected: Node 0 has highest betweenness, leaves have 0")

# %% Test execution
betweenness_values = compute_betweenness_centrality(g_star)
print(f"\n[Result] Computed betweenness values: {betweenness_values}")

# %% Test 1: Function returns correct type
print("\n[Test 3.1] Checking return type")
assert isinstance(
    betweenness_values, (list, np.ndarray)
), f"compute_betweenness_centrality should return a list or array, got {type(betweenness_values)}"
print("✓ Returns list or array")

# %% Test 2: Correct number of values
print("\n[Test 3.2] Checking number of values")
assert (
    len(betweenness_values) == 5
), f"Expected 5 betweenness values for 5 nodes, got {len(betweenness_values)}"
print("✓ Returns correct number of values")

# %% Test 3: Center node has highest betweenness
print("\n[Test 3.3] Checking center node has highest betweenness")
max_betweenness_node = np.argmax(betweenness_values)
assert (
    max_betweenness_node == 0
), f"Center node (0) should have highest betweenness, but node {max_betweenness_node} does"
print(f"✓ Node {max_betweenness_node} has highest betweenness")

# %% Test 4: Center node has positive betweenness
print("\n[Test 3.4] Checking center node betweenness value")
assert (
    betweenness_values[0] > 0
), f"Center node should have positive betweenness, got {betweenness_values[0]}"
print(f"✓ Center node has betweenness {betweenness_values[0]:.4f}")

# %% Test 5: Leaf nodes have 0 betweenness
print("\n[Test 3.5] Checking leaf nodes have 0 betweenness")
for i in range(1, 5):
    assert (
        betweenness_values[i] == 0
    ), f"Leaf node {i} should have betweenness 0, got {betweenness_values[i]}"
print("✓ All leaf nodes have betweenness 0")

# %% Summary
print("\n" + "=" * 60)
print("All tests passed for Task 3! ✓")
print("=" * 60)
