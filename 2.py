import numpy as np
import plotly.graph_objects as go

# Load the data
file_path = '4.npy'  # Replace with your actual file path
data = np.load(file_path)

# Define the joints and their connections
joints = ['Hip (root)', 'Right hip', 'Right knee', 'Right foot', 'Left hip', 'Left knee', 'Left foot', 
          'Spine', 'Thorax', 'Nose', 'Head', 'Left shoulder', 'Left elbow', 'Left wrist', 
          'Right shoulder', 'Right elbow', 'Right wrist']

connections = [
    ('Hip (root)', 'Spine'), ('Spine', 'Thorax'), 
    ('Thorax', 'Left shoulder'), ('Left shoulder', 'Left elbow'), ('Left elbow', 'Left wrist'),
    ('Thorax', 'Right shoulder'), ('Right shoulder', 'Right elbow'), ('Right elbow', 'Right wrist'),
    ('Hip (root)', 'Left hip'), ('Left hip', 'Left knee'), ('Left knee', 'Left foot'),
    ('Hip (root)', 'Right hip'), ('Right hip', 'Right knee'), ('Right knee', 'Right foot'),
    ('Thorax', 'Nose'), ('Nose', 'Head'),('Head', 'Head')
]

# Initialize figure
fig = go.Figure()

# Add 3D scatter plot for joints
scatter = fig.add_scatter3d(x=data[0, :, 0], y=data[0, :, 1], z=data[0, :, 2],
                            mode='markers', name='Joints')

# Add lines for connections
lines = []
for start, end in connections:
    start_idx = joints.index(start)
    end_idx = joints.index(end)
    line = fig.add_scatter3d(x=[data[0, start_idx, 0], data[0, end_idx, 0]],
                             y=[data[0, start_idx, 1], data[0, end_idx, 1]],
                             z=[data[0, start_idx, 2], data[0, end_idx, 2]],
                             mode='lines', line=dict(color='blue', width=4))
    lines.append(line)

# Create a frame for each time step
frames = []
for frame_data in data:
    frame_lines = []
    for start, end in connections:
        start_idx = joints.index(start)
        end_idx = joints.index(end)
        frame_line = go.Scatter3d(x=[frame_data[start_idx, 0], frame_data[end_idx, 0]],
                                  y=[frame_data[start_idx, 1], frame_data[end_idx, 1]],
                                  z=[frame_data[start_idx, 2], frame_data[end_idx, 2]],
                                  mode='lines', line=dict(color='blue', width=4))
        frame_lines.append(frame_line)
    frames.append(frame_lines)


x_min, x_max = np.min(data[:,:,0]), np.max(data[:,:,0])
y_min, y_max = np.min(data[:,:,1]), np.max(data[:,:,1])
z_min, z_max = np.min(data[:,:,2]), np.max(data[:,:,2])


# Define animation settings
animation_settings = dict(frame=dict(duration=50, redraw=True), fromcurrent=True)

# Add frames to figure
fig.frames = [go.Frame(data=frame, name=str(i)) for i, frame in enumerate(frames)]

# Add slider for animation control
sliders = [dict(steps=[dict(args=[[f.name], animation_settings], label=str(i), method='animate')
                       for i, f in enumerate(fig.frames)], active=0)]

# Update layout to include slider and axis labels
fig.update_layout(
    updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                            method='animate', args=[None, animation_settings])])],
    sliders=sliders,
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',  # This line ensures x:y:z = 1:1:1
        xaxis=dict(range=[-1, 1]),
        yaxis=dict(range=[-1, 1]),
        zaxis=dict(range=[-1, 1])
    )
)

# Show figure
fig.show()

