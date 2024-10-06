import streamlit as st
import plotly.graph_objects as go

# Title of the app
st.title('Interactive Solar System')

# Create a 3D scatter plot for the solar system
fig = go.Figure()

# Data for the planets
planets = {
    'Mercury': {'distance': 57.9, 'size': 0.383, 'color': 'gray'},
    'Venus': {'distance': 108.2, 'size': 0.949, 'color': 'gold'},
    'Earth': {'distance': 149.6, 'size': 1.0, 'color': 'blue'},
    'Mars': {'distance': 227.9, 'size': 0.532, 'color': 'red'},
    'Jupiter': {'distance': 778.3, 'size': 11.21, 'color': 'orange'},
    'Saturn': {'distance': 1427, 'size': 9.45, 'color': 'goldenrod'},
    'Uranus': {'distance': 2871, 'size': 4.01, 'color': 'lightblue'},
    'Neptune': {'distance': 4497.1, 'size': 3.88, 'color': 'darkblue'}
}

# Add the Sun at the center
fig.add_trace(go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode='markers',
    marker=dict(size=30, color='yellow', line=dict(width=2)),
    name='Sun'
))

# Add planets to the plot
for planet, data in planets.items():
    fig.add_trace(go.Scatter3d(
        x=[data['distance']],
        y=[0],
        z=[0],
        mode='markers+text',
        marker=dict(size=data['size']*10, color=data['color'], line=dict(width=2)),
        text=planet,
        textposition='top center',
        hoverinfo='text',
        hovertemplate=f'{planet}<br>Distance: {data["distance"]} million km<br>Size: {data["size"]} Earth diameters'
    ))

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='Distance from Sun (million km)',
        yaxis_title='',
        zaxis_title='',
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=0.1)
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False,
    paper_bgcolor='black',
    plot_bgcolor='black'
)

# Add background stars for a space effect
fig.add_trace(go.Scatter3d(
    x=[x for x in range(50)],
    y=[y for y in range(50)],
    z=[z for z in range(50)],
    mode='markers',
    marker=dict(size=2, color='white', opacity=0.5)
))

# Display the plot
st.plotly_chart(fig)
