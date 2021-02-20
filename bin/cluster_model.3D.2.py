#!/usr/bin/env python3


########
#
#   cluster_model.3D.2.py
#
#   Author: YU Hao  (yuhao@genomics.cn)
#
#   Date:   2020-5-21   (v1.0)
#
########




import sys

import plotly.graph_objects as go

import datatable as dt
from datatable import f

import numpy as np




dfMeta = dt.fread(sys.argv[1])


traces = []

catalogue = 'V1'

x1 = dfMeta[f.region != catalogue, 'UMAP1'].to_list()[0]
y1 = dfMeta[f.region != catalogue, 'UMAP2'].to_list()[0]
z1 = dfMeta[f.region != catalogue, 'UMAP3'].to_list()[0]

x2 = dfMeta[f.region == catalogue, 'UMAP1'].to_list()[0]
y2 = dfMeta[f.region == catalogue, 'UMAP2'].to_list()[0]
z2 = dfMeta[f.region == catalogue, 'UMAP3'].to_list()[0]

tip = catalogue

traces.append(
    go.Scatter3d(
        name=catalogue,

        x=x1,
        y=y1,
        z=z1,

        mode='markers',
        marker=dict(
        
            size=1,
            color='lightgrey',
            line=dict(width=0, color='white'),
            opacity=0.5

        ),
        hoverinfo='text',
        hovertext=tip,

        showlegend=False
    )
)

traces.append(
    go.Scatter3d(
        name=catalogue,

        x=x2,
        y=y2,
        z=z2,

        mode='markers',
        marker=dict(
        
            size=1,
            color=dfMeta[f.region == catalogue, 'region_color'].to_list()[0],
            line=dict(width=0, color='white'),
            opacity=1

        ),
        hoverinfo='text',
        hovertext=tip,

        showlegend=False
    )
)


R = 2


layout = go.Layout(

    autosize=False,
    width=1000,
    height=1000,

    scene=dict(

        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),

        camera=dict(
            eye=dict(
                x=R,
                y=0, 
                z=0
            )
        )

    )

)


x = R * np.cos(np.asarray([_ for _ in range(0, 360)]) * (np.pi / 180))
y = R * np.sin(np.asarray([_ for _ in range(0, 360)]) * (np.pi / 180))

for i in range(270, 360):

    X = x[i]
    Y = y[i]

    layout['scene']['camera']['eye'] = dict(x=X, y=Y, z=0)


    fig = go.Figure(data=traces, layout=layout)
    fig.write_image('demo/demo.' + '%02d' % i + '.png')