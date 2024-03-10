import streamlit as st
from matplotlib import animation
import matplotlib.pyplot as plt

# Define the path as an array of vertex indices
path = [1, 4, 3, 2, 3]

# Create a dictionary to map vertex indices to coordinates (replace with actual coordinates)
vertex_coordinates = {
    1: (1, 5),
    2: (7, 2),
    3: (4, 1),
    4: (2, 8),
}

# Function to update the animation frame
def animate(i):
    # Clear the plot
    plt.cla()

    # Print current step and vertices being drawn (for debugging)
    print(f"Step: {i+1}, Path: {path[:i+1]}")

    # Draw the path up to the current index
    for j in range(i):
        start_x, start_y = vertex_coordinates[path[j]]
        end_x, end_y = vertex_coordinates[path[j + 1]]
        plt.plot([start_x, end_x], [start_y, end_y], color='blue', marker='o')  # Draw lines and markers

    # Draw all vertices as circles
    for vertex, (x, y) in vertex_coordinates.items():
        plt.plot(x, y, 'o', markersize=15, color='green')
        plt.text(x, y + 0.2, f"v{vertex}", ha='center', va='center', fontsize=12)  # Label vertices

    plt.xlim(0, 10)  # Set plot limits
    plt.ylim(0, 10)
    plt.title(f"Path Animation: Step {i+1}")

    return plt.gcf()  # Return the updated figure

# Create the animation object
fig, ax = plt.subplots()
anim = animation.FuncAnimation(fig, animate, frames=len(path), interval=1000)  # 1 second interval

# Try plotting vertices statically for verification (optional)
# plt.scatter(list(vertex_coordinates.values())[:, 0], list(vertex_coordinates.values())[:, 1])
# plt.show()

# Display the animation on Streamlit
st.write("Animated Path")
st.pyplot(fig)
