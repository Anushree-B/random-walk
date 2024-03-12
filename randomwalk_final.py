import networkx as nx
import random
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 

st.set_option('deprecation.showPyplotGlobalUse', False)

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

# After defining the graph (graph)
fig, ax = plt.subplots()
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
nx.draw(graph, with_labels=True, font_weight='bold')
plt.axis('off')  # Remove unnecessary axis


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

st.pyplot()
# Perform a random walk starting from a random node with 5 steps
walk_result=[]
start_node = st.button("Click to start random walk from a random node")
if start_node:
    start_node = random.choice(list(graph.nodes))
    walk_result = random_walk(graph, start_node, steps=5)



st.write("Random Walk:", walk_result)

G = nx.MultiDiGraph()
arr=[]
for i in range(len(walk_result)-1):
    arr.append((walk_result[i],walk_result[i+1]))
print(arr)

G.add_edges_from(arr)

pos=nx.spring_layout(G,seed=5)



# Show the plot using Streamlit
if start_node:
    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    st.pyplot()
