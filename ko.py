import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Load the numpy file
file_path = 'outputfile.npy'  # Replace with the path to your NumPy file
data = np.load(file_path)

# Define the list of joints as provided
joints = ['Hip (root)', 'Right hip', 'Right knee', 'Right foot', 'Left hip', 'Left knee', 'Left foot', 
          'Spine', 'Thorax', 'Nose', 'Head', 'Left shoulder', 'Left elbow', 'Left wrist', 
          'Right shoulder', 'Right elbow', 'Right wrist']

# Define the connections between joints
connections = [
    ('Hip (root)', 'Right hip'), ('Right hip', 'Right knee'), ('Right knee', 'Right foot'),
    ('Hip (root)', 'Left hip'), ('Left hip', 'Left knee'), ('Left knee', 'Left foot'),
    ('Hip (root)', 'Spine'), ('Spine', 'Thorax'),
    ('Thorax', 'Nose'), ('Nose', 'Head'),
    ('Thorax', 'Left shoulder'), ('Left shoulder', 'Left elbow'), ('Left elbow', 'Left wrist'),
    ('Thorax', 'Right shoulder'), ('Right shoulder', 'Right elbow'), ('Right elbow', 'Right wrist')
]

# Function to plot skeleton for a given frame
def plot_skeleton(frame_data, ax):
    ax.clear()
    for connection in connections:
        pt1, pt2 = connection
        idx1, idx2 = joints.index(pt1), joints.index(pt2)
        coord1, coord2 = frame_data[idx1], frame_data[idx2]
        ax.plot([coord1[0], coord2[0]], [coord1[1], coord2[1]], [coord1[2], coord2[2]], 'bo-')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initial plot
plot_skeleton(data[0], ax)

# Add a slider for frames
ax_slider = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Frame', 0, len(data)-1, valinit=0, valstep=1)

# Update function for slider
def update(val):
    frame = int(slider.val)
    plot_skeleton(data[frame], ax)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()