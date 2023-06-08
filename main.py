import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Anime EDA")
st.markdown("Here is our EDA on Anime!")

df = pd.read_csv('https://raw.githubusercontent.com/ayang903/algorithmic-armadillos/main/anime.csv')

st.dataframe(df)
st.text('basically, ')
columns_drop = ['broadcast_day', 'broadcast_time', 'background', 'trailer_url', 'title_english']
df.drop(columns_drop, axis=1, inplace=True)
df.dropna(subset = ['score', 'source'], inplace=True)

#Amelia
grouped_df = df.groupby('type')['score'].mean()

grouped_df = grouped_df.sort_values(ascending=False)

fig = px.bar(
    x = grouped_df.index,
    y = grouped_df.values,
    color = grouped_df.values,
)

fig.update_layout (
    title ='Average Score by Media Type',
    xaxis_title = "Media Type",
    yaxis_title = "Average Score"

)

fig.update_yaxes(range = [ 5.5, 7])
st.plotly_chart(fig)
st.markdown("this graph shows this")

status_counts = df['status'].value_counts()

labels = status_counts.index.tolist()
values = status_counts.values.tolist()

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig.update_layout(
    title='Airing Status')
st.plotly_chart(fig)
st.markdown("this one shows that")
st.write('hi')
