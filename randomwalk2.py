import networkx as nx
import random
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import base64
from io import BytesIO

st.title("Random walk")

# Create an undirected graph with unit edges
graph = nx.Graph()

v = st.number_input("Enter the number of vertices:", min_value=1, value=5, step=1)
e = st.number_input("Enter the number of edges:", min_value=1, value=5, step=1)
arr = []

for i in range(e):
    v1 = st.number_input(f"Enter v1 for the {i+1}th edge", min_value=1, value=1, step=1)
    v2 = st.number_input(f"Enter v2 for the {i+1}th edge", min_value=1, value=2, step=1)
    arr.append((v1, v2))

# Add edges to the graph (you can customize this based on your specific graph)
graph.add_edges_from(arr)

# Function to perform a random walk on the graph
def random_walk(graph, start_node, steps):
    current_node = start_node
    walk_sequence = [current_node]

    for _ in range(steps):
        neighbors = list(graph.neighbors(current_node))
        if not neighbors:
            break

        next_node = random.choice(neighbors)
        walk_sequence.append(next_node)
        current_node = next_node

    return walk_sequence

# Function to animate the random walk
def animate_random_walk(graph, walk_sequence):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph)  # You can customize the layout algorithm

    def update(frame):
        ax.clear()
        nx.draw(graph, pos, ax=ax, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray')
        nx.draw_networkx_nodes(graph, pos, nodelist=[walk_sequence[frame]], node_color='red', node_size=500)

    ani = animation.FuncAnimation(fig, update, frames=len(walk_sequence), repeat=False)
    
    # Save the animation as a GIF
    buffer = BytesIO()
    ani.save(buffer, writer='pillow', fps=1)  # Specify the writer and frames per second
    buffer.seek(0)

    # Encode the GIF file as base64
    ani_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Display the base64-encoded animation in Streamlit
    st.image(ani_base64, format='png')

    plt.close(fig)  # Close the Matplotlib figure to avoid conflicts

# Perform a random walk starting from a random node with 5 steps
start_node = st.button("Click to start random walk from a random node")
if start_node:
    start_node = random.choice(list(graph.nodes))
    walk_result = random_walk(graph, start_node, steps=5)

    st.write("Random Walk:", walk_result)
    animate_random_walk(graph, walk_result)
