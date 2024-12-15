import numpy as np
import plotly.graph_objects as go

def load_and_plot(file_path, color, name_prefix, connections, joints):
    data = np.load(file_path)
    frames = []
    
    # Add lines for connections
    for frame_data in data:
        frame_lines = []
        for start, end in connections:
            start_idx = joints.index(start)
            end_idx = joints.index(end)
            frame_line = go.Scatter3d(x=[frame_data[start_idx, 0], frame_data[end_idx, 0]],
                                      y=[frame_data[start_idx, 1], frame_data[end_idx, 1]],
                                      z=[frame_data[start_idx, 2], frame_data[end_idx, 2]],
                                      mode='lines', line=dict(color=color, width=4),
                                      name=f"{name_prefix}_{start}_{end}")
            frame_lines.append(frame_line)
        frames.append(frame_lines)
    
    return frames

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

# Load and plot the first dataset
frames1 = load_and_plot('4.npy', 'blue', 'Dataset1', connections, joints)

# Load and plot the second dataset
frames2 = load_and_plot('5.npy', 'red', 'Dataset2', connections, joints)

# Merge frames from both datasets for each time step
frames = [f1 + f2 for f1, f2 in zip(frames1, frames2)]

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
