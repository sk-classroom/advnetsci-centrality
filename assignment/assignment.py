import marimo

__generated_with = "0.14.17"
app = marimo.App(width="full")

with app.setup(hide_code=True):
    # Initialization code that runs before all other cells
    import numpy as np
    import igraph


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Centrality Measures Assignment

    Welcome to the **BCDE Graph Challenge**!

    In this assignment, you'll create a graph where the most central node is **different** for each of four centrality measures: **B**etweenness, **C**loseness, **D**egree, and **E**ccentricity.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 📋 Assignment Instructions & Grading""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "📋 Assignment Tasks": mo.md(
                r"""
            Complete the following tasks and upload your notebook to your GitHub repository.

            1. **Task 1**: Implement `compute_degree_centrality` to return degree centrality values for all nodes
            2. **Task 2**: Implement `compute_closeness_centrality` to return closeness centrality values for all nodes
            3. **Task 3**: Implement `compute_betweenness_centrality` to return betweenness centrality values for all nodes
            4. **Task 4**: Implement `compute_eccentricity_centrality` to return eccentricity values for all nodes
            5. **Task 5**: Create a BCDE graph where all four most central nodes are different
            6. Update this notebook by using `git add`, `git commit`, and then `git push`.
            7. The notebook will be automatically graded, and your score will be shown on GitHub.

            **Important**: For Task 5, ensure that no two nodes have the same maximum/minimum centrality value. Each centrality measure must have a unique node with the highest (or lowest for eccentricity) value - no ties allowed!
            """
            ),
            "🔒 Protected Files": mo.md(
                r"""
            Protected files are test files and configuration files you cannot modify. They appear in your repository but don't make any changes to them.
            """
            ),
            "⚖️ Academic Integrity": mo.md(
                r"""
            There is a system that automatically checks code similarity across all submissions and online repositories. Sharing code or submitting copied work will result in zero credit and disciplinary action.

            While you can discuss concepts, each student must write their own code. Cite any external resources, including AI tools, in your comments.
            """
            ),
            "📚 Allowed Libraries": mo.md(
                r"""
            You **cannot** import any other libraries that result in the grading script failing or a zero score. Only use: `numpy`, `igraph`, `altair`, `pandas`, `marimo`
            """
            ),
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 1: Degree Centrality

    Implement a function that returns the **degree centrality values** for all nodes.

    Degree centrality counts the number of edges connected to a node.
    """
    )
    return


@app.function
# Task 1
def compute_degree_centrality(g):
    """
    Compute degree centrality for all nodes.

    Args:
        g (igraph.Graph): Input graph

    Returns:
        list or array: Degree centrality values for all nodes
    """
    return ...


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 2: Closeness Centrality

    Implement a function that returns the **closeness centrality values** for all nodes.

    Closeness centrality measures how close a node is to all other nodes (inverse of average shortest path length).
    """
    )
    return


@app.function
# Task 2
def compute_closeness_centrality(g):
    """
    Compute closeness centrality for all nodes.

    Args:
        g (igraph.Graph): Input graph (should be connected)

    Returns:
        list or array: Closeness centrality values for all nodes
    """
    return ...


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 3: Betweenness Centrality

    Implement a function that returns the **betweenness centrality values** for all nodes.

    Betweenness centrality measures how often a node lies on shortest paths between other nodes.
    """
    )
    return


@app.function
# Task 3
def compute_betweenness_centrality(g):
    """
    Compute betweenness centrality for all nodes.

    Args:
        g (igraph.Graph): Input graph

    Returns:
        list or array: Betweenness centrality values for all nodes
    """
    return ...


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 4: Eccentricity Centrality

    Implement a function that returns the **eccentricity values** for all nodes.

    Eccentricity is the maximum shortest path distance from a node to any other node. Lower eccentricity means more central.
    """
    )
    return


@app.function
# Task 4
def compute_eccentricity_centrality(g):
    """
    Compute eccentricity for all nodes.

    Args:
        g (igraph.Graph): Input graph (should be connected)

    Returns:
        list or array: Eccentricity values for all nodes
    """
    return g.eccentricity()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 5: Create a BCDE Graph

    Create a connected graph where:
    - The node with maximum **B**etweenness centrality
    - The node with maximum **C**loseness centrality
    - The node with maximum **D**egree centrality
    - The node with minimum **E**ccentricity

    are **all different nodes**.

    **Important constraints**:
    - Each centrality measure must have exactly **one** node with the maximum (or minimum for eccentricity) value
    - **No ties allowed**: Multiple nodes cannot share the same maximum/minimum centrality value
    - The graph must be **connected** (all nodes reachable from any other node)

    Return the graph as an edge list (list of tuples).
    """
    )
    return


@app.function
# Task 5


def create_bcde_graph():
    """
    Create a BCDE graph.

    The graph should be connected and have different nodes as the most central
    for each of the four centrality measures.

    Returns:
        list: Edge list as a list of tuples [(source, target), ...]
              where the most central nodes differ across betweenness,
              closeness, degree, and eccentricity

    Hint:
      1. Start with a single line of four nodes: 0--1--2--3
      2. Then, add edges to node 0 to make it a degree hub
      3. Extend the graph by creating a tree rooted from node 3, until node 3 becomes the most central in terms of the betweeness
      4. Add edges or nodes such that the central nodes in terms of the closeness and eccentricity are different.

    """
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]  # line graph

    return edges


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    ## Your graph
    """
    )
    return


@app.cell(hide_code=True)
def _(
    g,
    graph_layout,
    mo,
    most_central_betweenness,
    most_central_closeness,
    most_central_degree,
    most_central_eccentricity,
    validation_message,
    visualize_bcde_graph,
):
    # Always display the visualization with consistent layout
    fig = visualize_bcde_graph(
        g,
        most_central_degree,
        most_central_closeness,
        most_central_betweenness,
        most_central_eccentricity,
        graph_layout,
    )

    # Show validation message with appropriate style
    if "✅" in validation_message:
        callout_kind = "success"
    else:
        callout_kind = "warn"

    ret = mo.hstack(
        [fig, mo.callout(validation_message, kind=callout_kind)],
        widths=[0.4, 0.3],
        justify="start",
        align="start",
    )
    ret
    return


@app.cell(hide_code=True)
def _(
    betweenness_values,
    closeness_values,
    degree_values,
    eccentricity_values,
    g,
    graph_layout,
    visualize_centrality_heatmaps,
):
    # Display the heatmap visualization with the same layout
    fig_heatmap = visualize_centrality_heatmaps(
        g,
        degree_values,
        closeness_values,
        betweenness_values,
        eccentricity_values,
        graph_layout,
    )
    fig_heatmap
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Libraries""")
    return


@app.cell(hide_code=True)
def _():
    # All imports in one place to avoid conflicts
    import altair as alt
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    return plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Code""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Create Graph from Edge List""")
    return


@app.cell(hide_code=True)
def _():
    # Create the graph from the edge list
    edge_list = create_bcde_graph()
    g = igraph.Graph(edges=edge_list, directed=False)

    # Create a consistent layout for all visualizations
    graph_layout = g.layout_fruchterman_reingold()
    return g, graph_layout


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Compute Centralities""")
    return


@app.cell(hide_code=True)
def _(g):
    # Compute centrality values for all nodes
    degree_values = compute_degree_centrality(g)
    closeness_values = compute_closeness_centrality(g)
    betweenness_values = compute_betweenness_centrality(g)
    eccentricity_values = compute_eccentricity_centrality(g)

    # Validate: Check for ties (multiple nodes with same max/min value)
    def check_unique_extremum(values, use_min=False):
        """Check if the maximum (or minimum) value appears only once."""
        arr = np.array(values)
        extreme_val = np.min(arr) if use_min else np.max(arr)
        count = np.sum(arr == extreme_val)
        return count == 1

    # Check for ties in each centrality measure
    has_degree_tie = not check_unique_extremum(degree_values)
    has_closeness_tie = not check_unique_extremum(closeness_values)
    has_betweenness_tie = not check_unique_extremum(betweenness_values)
    has_eccentricity_tie = not check_unique_extremum(eccentricity_values, use_min=True)

    # Always find the most central nodes for each measure
    most_central_degree = np.argmax(degree_values)
    most_central_closeness = np.argmax(closeness_values)
    most_central_betweenness = np.argmax(betweenness_values)
    most_central_eccentricity = np.argmin(eccentricity_values)  # min for eccentricity

    # Create validation message
    if (
        has_degree_tie
        or has_closeness_tie
        or has_betweenness_tie
        or has_eccentricity_tie
    ):
        tie_messages = []
        if has_degree_tie:
            tie_messages.append("degree centrality")
        if has_closeness_tie:
            tie_messages.append("closeness centrality")
        if has_betweenness_tie:
            tie_messages.append("betweenness centrality")
        if has_eccentricity_tie:
            tie_messages.append("eccentricity")

        validation_message = f"⚠️ Warning: Multiple nodes have the same highest/lowest value for: {', '.join(tie_messages)}. Showing one of the tied nodes. You must ensure unique maximum/minimum values for full credit."
    else:
        validation_message = (
            "✅ All centrality measures have unique maximum/minimum values."
        )
    return (
        betweenness_values,
        closeness_values,
        degree_values,
        eccentricity_values,
        most_central_betweenness,
        most_central_closeness,
        most_central_degree,
        most_central_eccentricity,
        validation_message,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Validation Results""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Visualization Function""")
    return


@app.cell(hide_code=True)
def _(plt, sns):
    def visualize_bcde_graph(
        g,
        most_central_degree,
        most_central_closeness,
        most_central_betweenness,
        most_central_eccentricity,
        layout,
    ):
        """
        Visualize the BCDE graph with nodes colored by their centrality role.

        Args:
            g: igraph.Graph object
            most_central_degree: node ID with max degree centrality
            most_central_closeness: node ID with max closeness centrality
            most_central_betweenness: node ID with max betweenness centrality
            most_central_eccentricity: node ID with min eccentricity
            layout: graph layout to use for consistency
        """
        import igraph
        from matplotlib.patches import Patch

        # Create a vibrant color palette using seaborn
        palette = sns.color_palette("colorblind", 4)

        # Map nodes to colors based on their centrality role
        node_colors = ["#E8E8E8"] * g.vcount()  # Light gray for non-central nodes
        node_labels = [""] * g.vcount()

        # Assign colors for most central nodes (only if not None)
        centrality_map = {
            most_central_degree: (palette[0], "D (Degree)"),
            most_central_closeness: (palette[1], "C (Closeness)"),
            most_central_betweenness: (palette[2], "B (Betweenness)"),
            most_central_eccentricity: (palette[3], "E (Eccentricity)"),
        }

        for node_id, (color, label) in centrality_map.items():
            if node_id is not None:
                print(f"  Coloring node {node_id} with {label}")
                node_colors[node_id] = color
                node_labels[node_id] = label

        # Create the plot
        fig, ax = plt.subplots(figsize=(6, 6))

        # Plot using igraph's plot
        visual_style = {
            "vertex_size": 40,
            "vertex_color": node_colors,
            "vertex_label": [
                f"{i}\n{node_labels[i]}" if node_labels[i] else str(i)
                for i in range(g.vcount())
            ],
            "vertex_label_size": 11,
            "vertex_label_color": "black",
            "vertex_frame_width": 2,
            "vertex_frame_color": "white",
            "edge_width": 2.5,
            "edge_color": "black",
            "layout": layout,
            "bbox": (500, 500),
            "margin": 60,
        }

        igraph.plot(g, target=ax, **visual_style)

        # Add title
        ax.set_title(
            "BCDE Graph: Most Central Nodes by Measure",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )

        # Create custom legend
        legend_elements = []
        if most_central_degree is not None:
            legend_elements.append(
                Patch(
                    facecolor=palette[0],
                    label=f"Degree: Node {most_central_degree}",
                    edgecolor="white",
                    linewidth=2,
                )
            )
        if most_central_closeness is not None:
            legend_elements.append(
                Patch(
                    facecolor=palette[1],
                    label=f"Closeness: Node {most_central_closeness}",
                    edgecolor="white",
                    linewidth=2,
                )
            )
        if most_central_betweenness is not None:
            legend_elements.append(
                Patch(
                    facecolor=palette[2],
                    label=f"Betweenness: Node {most_central_betweenness}",
                    edgecolor="white",
                    linewidth=2,
                )
            )
        if most_central_eccentricity is not None:
            legend_elements.append(
                Patch(
                    facecolor=palette[3],
                    label=f"Eccentricity: Node {most_central_eccentricity}",
                    edgecolor="white",
                    linewidth=2,
                )
            )
        legend_elements.append(
            Patch(
                facecolor="#E8E8E8", label="Other nodes", edgecolor="white", linewidth=2
            )
        )

        plt.tight_layout()
        return fig

    return (visualize_bcde_graph,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Centrality Heatmap Visualization""")
    return


@app.cell(hide_code=True)
def _(plt):
    def visualize_centrality_heatmaps(
        g,
        degree_values,
        closeness_values,
        betweenness_values,
        eccentricity_values,
        layout,
    ):
        """
        Visualize all four centrality measures in separate subplots with color gradients.

        Args:
            g: igraph.Graph object
            degree_values: degree centrality values
            closeness_values: closeness centrality values
            betweenness_values: betweenness centrality values
            eccentricity_values: eccentricity values
            layout: graph layout (for consistency with main visualization)
        """
        import igraph
        import matplotlib
        import matplotlib.cm as cm
        from matplotlib.colors import Normalize

        # Create figure with 2x2 subplots
        fig, axes = plt.subplots(1, 4, figsize=(12, 3))
        axes = axes.flatten()

        # Prepare centrality data
        centralities = [
            (degree_values, "Degree Centrality", False),
            (closeness_values, "Closeness Centrality", False),
            (betweenness_values, "Betweenness Centrality", False),
            (eccentricity_values, "Eccentricity", True),  # True means lower is better
        ]

        for idx, (values, title, invert) in enumerate(centralities):
            ax = axes[idx]

            # Normalize values for colormap
            values_array = np.array(values)

            norm = Normalize(vmin=values_array.min(), vmax=values_array.max())
            normalized_values = norm(values_array)

            # Get colors from Reds colormap
            if invert:
                cmap = matplotlib.colormaps["cividis_r"]
            else:
                cmap = matplotlib.colormaps["cividis"]

            colors = [cmap(val) for val in normalized_values]

            # Create visual style
            visual_style = {
                "vertex_size": 10,
                "vertex_color": colors,
                "vertex_label_size": 12,
                "vertex_label_color": "black",
                "edge_width": 2,
                "edge_color": "gray",
                "layout": layout,
                "bbox": (400, 350),
                "margin": 40,
            }

            # Plot
            igraph.plot(g, target=ax, **visual_style)
            ax.set_title(title, fontsize=14, fontweight="bold", pad=10)

            # Add colorbar
            sm = cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
            if invert:
                cbar.set_label("Lower is more central", rotation=270, labelpad=20)
            else:
                cbar.set_label("Higher is more central", rotation=270, labelpad=20)

        plt.tight_layout()
        return fig

    return (visualize_centrality_heatmaps,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### ...""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Filter Data""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Create Visualization""")
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
