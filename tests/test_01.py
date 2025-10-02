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

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import student function
import importlib.util

spec = importlib.util.spec_from_file_location("assignment", "assignment/assignment.py")
# spec = importlib.util.spec_from_file_location("assignment", "assignment.py")
assignment_module = importlib.util.module_from_spec(spec)
print(assignment_module)
spec.loader.exec_module(assignment_module)

compute_degree_centrality = assignment_module.compute_degree_centrality

print("=" * 60)
print("Test 1: Degree Centrality")
print("=" * 60)

# %% Test Setup
# Create a simple star graph: node 0 is center, connected to all others
g_star = igraph.Graph.Star(5, mode="undirected")
print(f"\n[Setup] Created star graph with 5 nodes")
print(f"  Node 0 (center) is connected to nodes 1, 2, 3, 4")
print(f"  Expected degrees: [4, 1, 1, 1, 1]")

# %% Test execution
degree_values = compute_degree_centrality(g_star)
print(f"\n[Result] Computed degree values: {degree_values}")

# %% Test 1: Function returns correct type
print("\n[Test 1.1] Checking return type")
assert isinstance(
    degree_values, (list, np.ndarray)
), f"compute_degree_centrality should return a list or array, got {type(degree_values)}"
print("✓ Returns list or array")

# %% Test 2: Correct number of values
print("\n[Test 1.2] Checking number of values")
assert (
    len(degree_values) == 5
), f"Expected 5 degree values for 5 nodes, got {len(degree_values)}"
print("✓ Returns correct number of values")

# %% Test 3: Center node has highest degree
print("\n[Test 1.3] Checking center node has highest degree")
max_degree_node = np.argmax(degree_values)
assert (
    max_degree_node == 0
), f"Center node (0) should have highest degree, but node {max_degree_node} does"
print(f"✓ Node {max_degree_node} has highest degree")

# %% Test 4: Center node degree value
print("\n[Test 1.4] Checking center node degree value")
assert (
    degree_values[0] == 4
), f"Center node should have degree 4, got {degree_values[0]}"
print(f"✓ Center node has degree {degree_values[0]}")

# %% Test 5: Leaf nodes have degree 1
print("\n[Test 1.5] Checking leaf nodes have degree 1")
for i in range(1, 5):
    assert (
        degree_values[i] == 1
    ), f"Leaf node {i} should have degree 1, got {degree_values[i]}"
print("✓ All leaf nodes have degree 1")

# %% Summary
print("\n" + "=" * 60)
print("All tests passed for Task 1! ✓")
print("=" * 60)
