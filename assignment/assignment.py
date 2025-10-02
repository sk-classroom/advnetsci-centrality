import marimo

__generated_with = "0.14.16"
app = marimo.App(width="full", theme="dark")

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
    mo.md(
        r"""
    # 📋 Assignment Instructions & Grading
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "📋 Assignment Tasks": mo.md(
                r"""
            Complete the following tasks and upload your notebook to your GitHub repository.

            1. **Task 1**: Implement `compute_degree_centrality` to find the node with maximum degree centrality
            2. **Task 2**: Implement `compute_closeness_centrality` to find the node with maximum closeness centrality
            3. **Task 3**: Implement `compute_betweenness_centrality` to find the node with maximum betweenness centrality
            4. **Task 4**: Implement `compute_eccentricity_centrality` to find the node with minimum eccentricity
            5. **Task 5**: Create a BCDE graph with exactly 11 nodes where all four most central nodes are different
            6. Update this notebook by using `git add`, `git commit`, and then `git push`.
            7. The notebook will be automatically graded, and your score will be shown on GitHub.
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

    Implement a function that returns the node ID with the **maximum degree centrality**.

    Degree centrality counts the number of edges connected to a node.
    """
    )
    return


@app.function
# Task 1
def compute_degree_centrality(g):
    """
    Find the node with maximum degree centrality.

    Args:
        g (igraph.Graph): Input graph

    Returns:
        int: Node ID with maximum degree centrality
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 2: Closeness Centrality

    Implement a function that returns the node ID with the **maximum closeness centrality**.

    Closeness centrality measures how close a node is to all other nodes (inverse of average shortest path length).
    """
    )
    return


@app.function
# Task 2
def compute_closeness_centrality(g):
    """
    Find the node with maximum closeness centrality.

    Args:
        g (igraph.Graph): Input graph (should be connected)

    Returns:
        int: Node ID with maximum closeness centrality
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 3: Betweenness Centrality

    Implement a function that returns the node ID with the **maximum betweenness centrality**.

    Betweenness centrality measures how often a node lies on shortest paths between other nodes.
    """
    )
    return


@app.function
# Task 3
def compute_betweenness_centrality(g):
    """
    Find the node with maximum betweenness centrality.

    Args:
        g (igraph.Graph): Input graph

    Returns:
        int: Node ID with maximum betweenness centrality
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 4: Eccentricity Centrality

    Implement a function that returns the node ID with the **minimum eccentricity**.

    Eccentricity is the maximum shortest path distance from a node to any other node. Lower eccentricity means more central.
    """
    )
    return


@app.function
# Task 4
def compute_eccentricity_centrality(g):
    """
    Find the node with minimum eccentricity (most central).

    Args:
        g (igraph.Graph): Input graph (should be connected)

    Returns:
        int: Node ID with minimum eccentricity
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 5: Create a BCDE Graph

    Create a connected graph with **exactly 11 nodes** where:
    - The node with maximum **B**etweenness centrality
    - The node with maximum **C**loseness centrality
    - The node with maximum **D**egree centrality
    - The node with minimum **E**ccentricity

    are **all different nodes**.

    Return the graph as an igraph.Graph object.
    """
    )
    return


@app.function
# Task 5
def create_bcde_graph():
    """
    Create a BCDE graph with exactly 11 nodes.

    The graph should be connected and have different nodes as the most central
    for each of the four centrality measures.

    Returns:
        igraph.Graph: A graph with 11 nodes where the most central nodes differ
                      across betweenness, closeness, degree, and eccentricity
    """
    pass


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    ## Interactive Visualization

    Put the visualization to test the students' implementation here.
    """
    )
    return



@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Understanding the Visualization

    Reflect on the visualization and the assignment task.

    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Libraries""")
    return


@app.cell
def _():
    # All imports in one place to avoid conflicts
    import numpy as np
    import igraph
    import altair as alt
    import pandas as pd
    return alt, igraph, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Code""")
    return


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
