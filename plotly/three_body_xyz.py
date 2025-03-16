import numpy as np
import plotly.graph_objects as go
from PyQt5.QtGui.QTextCursor import position
from scipy.integrate import odeint

'''
import chart_studio
import chart_studio.plotly as py

username = 'lalithuriti'
api_key = 'WkltoYNWP7gEy8eWuRUI'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
'''

G = 6.67428e-11  # Universal Gravitation Constant | N m^2 kg^-2

masses = np.array([0.1e9, 0.6e8, 0.1e9, 0.2e9])

positions = np.array([
    [0.1, 0, 0.4],
    [0.2, 0.1, 0],
    [-0.1, 0, -0.1],
    [0, 0.2, 0.3]
])  # km


velocities = np.array([
    [0.02, -0.02, 0.08],
    [0.1, 0.1, -0.02],
    [-0.04, -0.175, -0.01],
    [0.05, -0.1, 0.03]
])  # km/s

# Flatten because ODE solver needs a 1D array
init_params = np.concatenate([positions.flatten(), velocities.flatten()])

def n_body(init_params, t, G, masses):
    n = len(masses)

    positions = init_params[:3 * n].reshape(n, 3) # This will extract the first 3 * n values (the positions) and reshape them into 2D XYZ arrays
    velocities = init_params[3 * n:].reshape(n, 3) # Same thing but from the other way round

    # Compute derivatives kinematics stuff
    # dr/dt = velocity and dv_dt is acceleration
    dr_dt = velocities
    dv_dt = np.zeros_like(velocities)



    return np.array([dr_a_dt, dr_b_dt, dr_c_dt, dv_a_dt, dv_b_dt, dv_c_dt]).flatten()


init_params = np.array([r_a, r_b, r_c, v_a, v_b, v_c]).flatten()
print(init_params)

time_span = np.linspace(0, 200, 500)

three_body_sol = odeint(
    three_body, init_params, time_span, args=(G, m_a, m_b, m_c))


r_a_sol = three_body_sol[:, :3]
r_b_sol = three_body_sol[:, 3:6]
r_c_sol = three_body_sol[:, 6:9]

v_a_sol = three_body_sol[:, 9:12]
v_b_sol = three_body_sol[:, 12:15]
v_c_sol = three_body_sol[:, 15:18]


r_a_x_sol = np.array(r_a_sol[:, :1])
r_a_y_sol = np.array(r_a_sol[:, 1:2])
r_a_z_sol = np.array(r_a_sol[:, 2:3])

r_b_x_sol = np.array(r_b_sol[:, :1])
r_b_y_sol = np.array(r_b_sol[:, 1:2])
r_b_z_sol = np.array(r_b_sol[:, 2:3])

r_c_x_sol = np.array(r_c_sol[:, :1])
r_c_y_sol = np.array(r_c_sol[:, 1:2])
r_c_z_sol = np.array(r_c_sol[:, 2:3])


r_a_x_sol_ = r_a_x_sol[:, 0].tolist()
r_a_y_sol_ = r_a_y_sol[:, 0].tolist()
r_a_z_sol_ = r_a_z_sol[:, 0].tolist()

r_b_x_sol_ = r_b_x_sol[:, 0].tolist()
r_b_y_sol_ = r_b_y_sol[:, 0].tolist()
r_b_z_sol_ = r_b_z_sol[:, 0].tolist()

r_c_x_sol_ = r_c_x_sol[:, 0].tolist()
r_c_y_sol_ = r_c_y_sol[:, 0].tolist()
r_c_z_sol_ = r_c_z_sol[:, 0].tolist()


# Static Trajectory
three_body_plot_objects = []

r_a_trace = go.Scatter3d(
    x=r_a_x_sol_,
    y=r_a_y_sol_,
    z=r_a_z_sol_,
    name="Body A",
    mode='lines',
    line=dict(width=4))

three_body_plot_objects.append(r_a_trace)

r_b_trace = go.Scatter3d(
    x=r_b_x_sol_,
    y=r_b_y_sol_,
    z=r_b_z_sol_,
    name='Body B',
    mode='lines',
    line=dict(width=4))

three_body_plot_objects.append(r_b_trace)

r_c_trace = go.Scatter3d(
    x=r_c_x_sol_,
    y=r_c_y_sol_,
    z=r_c_z_sol_,
    name='Body C',
    mode='lines',
    line=dict(width=4))

three_body_plot_objects.append(r_c_trace)

three_body_plot_layout = go.Layout(title='Chaotic Evolution of a Three-Body System in Three-Dimensional Space', paper_bgcolor='#121922',
                                   plot_bgcolor='#121922',
                                   scene=dict(xaxis=dict(title='x (km)',
                                                         backgroundcolor='#121922',
                                                         color='white',
                                                         gridcolor='#1b2735'),
                                              yaxis=dict(title='y (km)',
                                                         backgroundcolor='#121922',
                                                         color='white',
                                                         gridcolor='#1b2735'),
                                              zaxis=dict(title='z (km)',
                                                         backgroundcolor='#121922',
                                                         color='white',
                                                         gridcolor='#1b2735'),
                                              camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0),
                                                          eye=dict(x=-1.25, y=-1.25, z=1.25))),
                                   font=dict(color="white")
                                   )

three_body_plot_xyz_static_traj = go.Figure(data=three_body_plot_objects,
                                            layout=three_body_plot_layout)

'''py.plot(three_body_plot_xyz_static_traj,
        filename='three_body_plot_xyz_static_traj', auto_open=True)'''

# three_body_plot_xyz_static_traj.show()


# Animated Trajectory
r_a_trace = go.Scatter3d(x=r_a_x_sol_[:2],
                         y=r_a_y_sol_[:2],
                         z=r_a_z_sol_[:2],
                         name='Body A',
                         mode='lines',
                         line=dict(width=4))

r_b_trace = go.Scatter3d(x=r_b_x_sol_[:2],
                         y=r_b_y_sol_[:2],
                         z=r_b_z_sol_[:2],
                         name='Body B',
                         mode='lines',
                         line=dict(width=4))

r_c_trace = go.Scatter3d(x=r_c_x_sol_[:2],
                         y=r_c_y_sol_[:2],
                         z=r_c_z_sol_[:2],
                         name='Body C',
                         mode='lines',
                         line=dict(width=4))

three_body_plot_trace_frames = [dict(data=[dict(type='scatter3d',
                                                x=r_a_x_sol_[: r + 1],
                                                y=r_a_y_sol_[: r + 1],
                                                z=r_a_z_sol_[: r + 1]),
                                           dict(type='scatter3d',
                                                x=r_b_x_sol_[: r + 1],
                                                y=r_b_y_sol_[: r + 1],
                                                z=r_b_z_sol_[: r + 1]),
                                           dict(type='scatter3d',
                                                x=r_c_x_sol_[: r + 1],
                                                y=r_c_y_sol_[: r + 1],
                                                z=r_c_z_sol_[: r + 1])],
                                     traces=[0, 1, 2],
                                     )for r in range(1, len(r_a_x_sol_))]

three_body_plot_layout = go.Layout(title='Chaotic Evolution of a Three-Body System in Three-Dimensional Space',
                                   paper_bgcolor='black',
                                   plot_bgcolor='rgba(0,0,0,0)',
                                   scene=dict(xaxis=dict(title='x (km)',
                                                         backgroundcolor='rgba(0,0,0,0)',
                                                         color='white',
                                                         gridcolor='white'),
                                              yaxis=dict(title='y (km)',
                                                         backgroundcolor='rgba(0,0,0,0)',
                                                         color='white',
                                                         gridcolor='white'),
                                              zaxis=dict(title='z (km)',
                                                         backgroundcolor='rgba(0,0,0,0)',
                                                         color='white',
                                                         gridcolor='white'),
                                              camera=dict(
                                                up=dict(x=0, y=0, z=9),
                                                center=dict(x=0, y=0, z=0),
                                                eye=dict(x=-1.25, y=-1.25, z=1.25))),
                                   updatemenus=[dict(type='buttons',
                                                     font=dict(
                                                         color='#1b2735'),
                                                     buttons=[dict(label='Play',
                                                                   method='animate',
                                                                   args=[None, dict(
                                                                       frame=dict(duration=3))])])],
                                   font=dict(color="white")
                                   )

three_body_plot_xyz_animated_traj = go.Figure(data=[r_a_trace, r_b_trace, r_c_trace],
                                              frames=three_body_plot_trace_frames, layout=three_body_plot_layout)

img_width = 7
img_height = 5
'''
py.plot(three_body_plot_xyz_animated_traj,
        filename='three_body_plot_xyz_animated_traj', auto_open=True)
'''
three_body_plot_xyz_animated_traj.add_layout_image(
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

three_body_plot_xyz_animated_traj.update_xaxes(showgrid=False, visible=False)
three_body_plot_xyz_animated_traj.update_yaxes(showgrid=False, visible=False)

three_body_plot_xyz_animated_traj.show()
