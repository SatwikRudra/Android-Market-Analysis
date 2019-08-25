
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('googleplaystore.csv')



#Graph of Category vs Rating
fig = px.scatter(df, x = 'Rating', y = 'Category')

fig.update_layout(
    
    title=go.layout.Title(
        text="Category vs Rating",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Rating",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Category",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    )
)
fig.update_xaxes(range=[0, 5])




#Graph of Category vs Price
fig2 = px.scatter(df, x = 'Price', y = 'Category')
fig2.update_layout(
    
    title=go.layout.Title(
        text="Category vs Price",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Price",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Category",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    )
)
fig2.update_xaxes(range=[0, 400])



#Graph of Type vs Installs
fig3 = px.box(df, x = 'Type', y = 'Installs')
fig3.update_layout(
    
    title=go.layout.Title(
        text="Type vs Installs",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Type",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Installs",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    )
)



#Graph of Size vs Installs
fig4 = px.scatter(df, x = 'Installs', y = 'Size')
fig4.update_layout(
    
    title=go.layout.Title(
        text="Size vs Installs",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Installs",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Size(M in MB,K in KB)",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#000000"
            )
        )
    )
)
fig.show()
fig2.show()
fig3.show()
fig4.show()