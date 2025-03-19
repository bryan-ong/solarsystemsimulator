import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go


# Constants
G = 6.67428e-11  # Universal Gravitational Constant | N m^2 kg^-2

# Number of bodies
n = 5  # Change this to the desired number of bodies

# Masses of the bodies (example values)
masses = np.array([0.1e9, 0.6e8, 0.1e9, 0.2e9, 0.5e7])[:n]  # kg

# Initial positions of the bodies
positions = np.array([
    [0.1, 0, 0.4],
    [0.2, 0.1, 0],
    [-0.1, 0, -0.1],
    [0, 0.2, 0.3],
    [0.25, 0.74, 0.3]
])[:n]  # km

# Initial velocities of the bodies
velocities = np.array([
    [0.02, -0.02, 0.08],
    [0.1, 0.1, -0.02],
    [-0.04, -0.175, -0.01],
    [0.05, -0.1, 0.03],
    [0.01, -0.2, -0.05]
])[:n]  # km/s

# Flatten initial conditions for ODE solver
init_params = np.concatenate([positions.flatten(), velocities.flatten()])

# Time span for the simulation
time_span = np.linspace(0, 200, 1000)


# N-body ODE function
def n_body_system(init_params, t, G, masses):
    n = len(masses)

    positions = init_params[:3 * n].reshape(n, 3)
    velocities = init_params[3 * n:].reshape(n, 3)

    # Compute derivatives kinematics stuff
    # dr/dt  =  velocity and dv_dt is acceleration
    dr_dt = velocities
    dv_dt = np.zeros_like(velocities)

    for i in range(n):
        for j in range(n):
            if i != j:  # Ensure that a body doesn't exert gravitational force upon itself
                r_ij = positions[j] - positions[i]  # Get distance between
                r_ij_norm = np.linalg.norm(r_ij)  # Get magnitude

                # We cannot use the typical formula for Newton's law of universal gravitation here as we are dealing with vectors
                # This means we need to multiply the formula with the unit vector which is the vector / magnitude
                dv_dt[i] += G * masses[j] * r_ij / r_ij_norm ** 3

    return np.concatenate([dr_dt.flatten(),
                           dv_dt.flatten()])  # Flattens and concatenates into 1D array for Ordinary Differential Equation Integrator below


# Solve the ODE
solution = odeint(n_body_system, init_params, time_span, args=(G, masses))

# Extract positions for each body
positions_sol = solution[:, :3 * n].reshape(-1, n, 3)

# Create traces for each body
traces = []
for i in range(n):
    trace_line = go.Scatter3d(
        x=positions_sol[:, i, 0],
        y=positions_sol[:, i, 1],
        z=positions_sol[:, i, 2],
        name=f'Body {i + 1} Trajectory',
        mode='lines',
        line=dict(width=2, color=f'hsl({i * 120}, 100%, 50%)')
    )
    traces.append(trace_line)

    trace_sphere = go.Scatter3d(
        x=[positions_sol[-1, i, 0]],
        y=[positions_sol[-1, i, 1]],
        z=[positions_sol[-1, i, 2]],
        name=f'Body {i + 1}',
        mode='markers',
        marker=dict(
            size=10,
            color=f'hsl({i * 120}, 100%, 50%)',
            opacity=0.8,
            symbol='circle'
        )
    )
    traces.append(trace_sphere)

frames = []
for r in range(len(time_span)):
    frame_data = []
    for i in range(n):
        frame_data.append(go.Scatter3d(
            x=positions_sol[:r + 1, i, 0],
            y=positions_sol[:r + 1, i, 1],
            z=positions_sol[:r + 1, i, 2],
            mode='lines',
            line=dict(width=2, color=f'hsl({i * 120}, 100%, 50%)'),
        ))
        frame_data.append(go.Scatter3d(
            x=[positions_sol[r, i, 0]],
            y=[positions_sol[r, i, 1]],
            z=[positions_sol[r, i, 2]],
            mode='markers',
            marker=dict(
                size=10,
                color=f'hsl({i * 120}, 100%, 50%)',
                opacity=0.8,
                symbol='circle'
            )
        ))
    frames.append(go.Frame(
        data=frame_data,
        name=f'frame{r}',
        layout=dict(
            annotations=[
                dict(
                    text=f'Time (Arbitrary): {time_span[r]:.1f}',
                    x=0,
                    y=0.5,
                    xref='paper',
                    yref='paper',
                    font=dict(size=16, color='white'),
                    showarrow=False
                )
            ]
        )
    ))


# Layout for the plot
layout = go.Layout(
    title='Chaotic Evolution of an N-Body System in Three-Dimensional Space',
    paper_bgcolor='black',
    plot_bgcolor='rgba(0,0,0,0)',
    scene=dict(
        xaxis=dict(title='x (km)', backgroundcolor='rgba(0,0,0,0)', color='white', gridcolor='white'),
        yaxis=dict(title='y (km)', backgroundcolor='rgba(0,0,0,0)', color='white', gridcolor='white'),
        zaxis=dict(title='z (km)', backgroundcolor='rgba(0,0,0,0)', color='white', gridcolor='white'),
        camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=-1.25, y=-1.25, z=1.25))),
    updatemenus=[dict(type='buttons',
                      font=dict(
                          color='#1b2735'),
                      buttons=[
                          dict(label='Play',
                               method='animate',
                               args=[None, dict(frame=dict(duration=(1000/60), redraw=True), fromcurrent=True)]),
                          # 60FPS
                          dict(label='Pause',
                               method='animate',
                               args=[[None], dict(mode="immediate")]),
                          dict(label='Next',
                               method='animate',
                               args=[None, dict(frame=dict(duration=0, redraw=True), fromcurrent=True,
                                                transition=dict(duration=0))]),
                          dict(label='Reset',
                               method='animate',
                               args=[None,
                                     dict(frame=dict(duration=0, redraw=True), fromcurrent=False, mode='immediate',
                                          transition=dict(duration=0))])
                      ])],
    sliders=[dict(
       active=0,
        # steps=slider_steps,
        currentvalue=dict(prefix='Time: ', font=dict(color='white')),
        len = 0.9,
        x=0.1,
        y=0,
        pad=dict(t=50, b=10)
    )],
    font=dict(color="white"),
    # uirevision='constant',
    # Seems that uirevision doesn't work for 3D scatter plots especially, this is meant to allow us to pan and zoom the camera while the animation is playing. Other people online also seem to have this issue
)

# Create the figure
fig = go.Figure(data=traces, frames=frames, layout=layout)

# Add background image
img_width = 7
img_height = 5
fig.add_layout_image(
    dict(
        source="https://cdn.mos.cms.futurecdn.net/HuGGeENt6kGyixe3hT9tnY.jpg",
        xref="x",
        yref="y",
        x=-1,
        y=4,
        sizex=img_width,
        sizey=img_height,
        sizing="fill",
        opacity=1,
        layer="below")
)

# Hide 2D axes
fig.update_xaxes(showgrid=False, visible=False)
fig.update_yaxes(showgrid=False, visible=False)

# Show the figure
fig.show()
