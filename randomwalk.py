import networkx as nx
import random
import streamlit as st
import matplotlib.pyplot as plt

st.title("Random walk")

# Create an undirected graph with unit edges
graph = nx.Graph()

v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
arr=[]
for i in range(e):
    v1 = int(input(f"Enter v1 for the i({i})th edge"))
    v2 = int(input(f"Enter v2 for the i({i})th edge"))
    arr.append((v1,v2))
# Add edges to the graph (you can customize this based on your specific graph)
graph.add_edges_from(arr)#[(1, 2), (2, 3), (3, 4), (4, 1), (1, 5)])

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

# Perform a random walk starting from a random node with 5 steps  
start_node = random.choice(list(graph.nodes))
walk_result = random_walk(graph, start_node, steps=5)

print("Random Walk:", walk_result)


nx.draw(graph)
plt.show()
