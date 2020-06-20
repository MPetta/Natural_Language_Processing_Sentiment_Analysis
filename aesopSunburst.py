#!/usr/bin/env python
# coding: utf-8

# In[70]:


import plotly.express as px
import pandas as pd

# read data
aesop = pd.read_csv('aesop_final_analysis.csv')
# rename column to remove space
aesop.rename(columns={'Song Title':'songTitle'}, inplace=True)
# get song count grouped by album and join that count back to dataframe with suffix
aesop = aesop.join(aesop.groupby('Album')['songTitle'].count(), on='Album', rsuffix='_cnt')
# get lists
root = ["Aesop"] * len(aesop.index)
count = aesop['songTitle_cnt'].tolist()
song = aesop['songTitle'].tolist()
lp = aesop['Album'].tolist()
year = aesop['Release Date'].tolist()
# assign subset object for printing
df = pd.DataFrame(
    dict(song=song, lp=lp, year=year, root=root, count=count)
)
# set up the sunburst plot
fig = px.sunburst(df, path=['root','year', 'lp', 'song'], values='count',
                  color_discrete_sequence=px.colors.qualitative.G10,
                  title="Songs from Albums over Years")
#fig.update_layout(title_text="Hover over the points to see the text")
fig.update_layout(title_x=0.5)
fig.write_html('songDash.html', auto_open=True)
fig.show()

