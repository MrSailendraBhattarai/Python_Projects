import plotly.graph_objects as go

def waterfall_chart(data, labels, title="Waterfall Chart"):
    # Create a list of values for the waterfall chart
    fig = go.Figure(go.Waterfall(
        orientation="v",  # "v" for vertical
        measure=["relative"] * len(data),  # All bars are relative to the previous
        x=labels,  # The x-axis labels
        y=data,  # The data values (positive/negative increments)
        text=data,  # Add data values as text on the bars
        hoverinfo="x+y+text",  # Hover information to display
        increasing={"marker":{"color":"green"}},  # Color for positive values
        decreasing={"marker":{"color":"red"}},  # Color for negative values
        totals={"marker":{"color":"blue"}}  # Color for the total bar
    ))

    # Update layout (title, axis labels, etc.)
    fig.update_layout(
        title=title,
        xaxis_title="Categories",
        yaxis_title="Values",
        showlegend=False
    )

    # Show the chart
    fig.show()

# Example data for the waterfall chart
data = [200, -50, 80, -30, 60]
labels = ['Start', 'Q1', 'Q2', 'Q3', 'End']

# Call the function to plot the chart
waterfall_chart(data, labels)
