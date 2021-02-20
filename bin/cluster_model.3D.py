#!/usr/bin/env python3


########
#
#   cluster_model.3D.py
#
#   Author: YU Hao  (yuhao@genomics.cn)
#
#   Date:   2020-4-21   (v1.0)
#
########




import sys

import plotly.graph_objects as go

import datatable as dt
from datatable import f

import numpy as np




dfMeta  = dt.fread(sys.argv[1])
dfColor = dt.fread(sys.argv[2])


traces = []

for catalogue in set(dfMeta['cell_type'].to_list()[0]):

    xs = dfMeta[f.cell_type == catalogue, 'UMAP1'].to_list()[0]
    ys = dfMeta[f.cell_type == catalogue, 'UMAP2'].to_list()[0]
    zs = dfMeta[f.cell_type == catalogue, 'UMAP3'].to_list()[0]

    tip = catalogue

    traces.append(
        go.Scatter3d(
            name=catalogue,

            x=xs,
            y=ys,
            z=zs,

            mode='markers',
            marker=dict(
            
                size=1,
                color=dfColor[f.cell_type == catalogue, 'color'].to_list()[0][0],
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

for i in range(0, 360):

    X = x[i]
    Y = y[i]

    layout['scene']['camera']['eye'] = dict(x=X, y=Y, z=0)


    fig = go.Figure(data=traces, layout=layout)
    fig.write_image('1.img/surface.' + '%03d' % i + '.png')
