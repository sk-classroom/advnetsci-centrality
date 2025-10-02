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

spec = importlib.util.spec_from_file_location(
    "for_instructor", "for_instructor/assignment.py"
)
assignment_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assignment_module)

create_bcde_graph = assignment_module.create_bcde_graph

print("=" * 60)
print("Test 5: BCDE Graph Creation")
print("=" * 60)

# %% Test Setup
print("\n[Setup] Testing create_bcde_graph function")
print("  Expected: A connected graph where B, C, D, E are all different nodes")

# %% Test execution
edge_list = create_bcde_graph()
print(f"\n[Result] Created graph with {len(edge_list)} edges")

# %% Test 1: Function returns a list
print("\n[Test 5.1] Checking return type")
assert isinstance(
    edge_list, list
), f"create_bcde_graph should return a list, got {type(edge_list)}"
print("✓ Returns a list")

# %% Test 2: Edge list is not empty
print("\n[Test 5.2] Checking edge list is not empty")
assert len(edge_list) > 0, "Edge list should not be empty"
print(f"✓ Edge list has {len(edge_list)} edges")

# %% Test 3: Edges are tuples/lists with 2 elements
print("\n[Test 5.3] Checking edge format")
for i, edge in enumerate(edge_list):
    assert isinstance(
        edge, (tuple, list)
    ), f"Edge {i} should be a tuple or list, got {type(edge)}"
    assert len(edge) == 2, f"Edge {i} should have 2 nodes, got {len(edge)}"
print("✓ All edges are valid tuples/lists with 2 nodes")

# %% Test 4: Create graph and check connectivity
print("\n[Test 5.4] Checking graph connectivity")
g_bcde = igraph.Graph(edges=edge_list, directed=False)
n_nodes = g_bcde.vcount()
print(f"  Graph has {n_nodes} nodes and {g_bcde.ecount()} edges")

assert g_bcde.is_connected(), "BCDE graph must be connected"
print("✓ Graph is connected")

# %% Test 5: Compute centralities
print("\n[Test 5.5] Computing centrality measures")
degree_vals = g_bcde.degree()
closeness_vals = g_bcde.closeness()
betweenness_vals = g_bcde.betweenness()
eccentricity_vals = g_bcde.eccentricity()

# Find most central nodes
most_central_degree = np.argmax(degree_vals)
most_central_closeness = np.argmax(closeness_vals)
most_central_betweenness = np.argmax(betweenness_vals)
most_central_eccentricity = np.argmin(eccentricity_vals)

print(f"\n  Most central nodes:")
print(
    f"    Degree (D):      Node {most_central_degree} (value={degree_vals[most_central_degree]})"
)
print(
    f"    Closeness (C):   Node {most_central_closeness} (value={closeness_vals[most_central_closeness]:.4f})"
)
print(
    f"    Betweenness (B): Node {most_central_betweenness} (value={betweenness_vals[most_central_betweenness]:.4f})"
)
print(
    f"    Eccentricity (E): Node {most_central_eccentricity} (value={eccentricity_vals[most_central_eccentricity]})"
)

# %% Test 6: All four most central nodes are different
print("\n[Test 5.6] Checking all four most central nodes are different")
central_nodes = {
    most_central_degree,
    most_central_closeness,
    most_central_betweenness,
    most_central_eccentricity,
}
assert (
    len(central_nodes) == 4
), f"All four most central nodes must be different. Got: D={most_central_degree}, C={most_central_closeness}, B={most_central_betweenness}, E={most_central_eccentricity}"
print(f"✓ All four nodes are different: {central_nodes}")

# %% Test 7: Check for uniqueness (no ties) - Warning only
print("\n[Test 5.7] Checking for ties in centrality values")


def check_unique_max(values):
    max_val = np.max(values)
    return np.sum(np.array(values) == max_val) == 1


def check_unique_min(values):
    min_val = np.min(values)
    return np.sum(np.array(values) == min_val) == 1


has_unique_degree = check_unique_max(degree_vals)
has_unique_closeness = check_unique_max(closeness_vals)
has_unique_betweenness = check_unique_max(betweenness_vals)
has_unique_eccentricity = check_unique_min(eccentricity_vals)

warnings = []
if not has_unique_degree:
    warnings.append("degree")
if not has_unique_closeness:
    warnings.append("closeness")
if not has_unique_betweenness:
    warnings.append("betweenness")
if not has_unique_eccentricity:
    warnings.append("eccentricity")

if warnings:
    print(f"⚠️  Warning: Ties detected in {', '.join(warnings)}")
    print("  Consider adjusting the graph to have unique maximum/minimum values")
else:
    print("✓ All centrality measures have unique maximum/minimum values (no ties)")

# %% Summary
print("\n" + "=" * 60)
print("All tests passed for Task 5! ✓")
print("=" * 60)
