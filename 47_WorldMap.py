
# World Map
# pip install plotly
import plotly.express as px

data = {
    'Country': ['United States', 'Canada', 'Brazil', 'Nepal', 'Russia'],
    'Value': [100, 80, 60, 40, 120]}

fig = px.choropleth(
    data_frame=data,
    locations='Country',
    locationmode='country names',
    color='Value',  
    title='World Map using Python',
    color_continuous_scale='Viridis'
)

# Show the map
fig.show()
