import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv('2023-10-09-lv-tulx.csv')
    return data

data = load_data()

st.title('eio. lahtine 23.')

st.subheader('Tulemused')
st.write(data)

st.sidebar.header('Data Exploration Options')

columns = st.sidebar.multiselect('Select Columns', data.columns.tolist(), default=["Koht", "Nimi", "Kool", "Kokku"])

selected_column = st.sidebar.selectbox('Filter Data by Column', data.columns.tolist(), index=data.columns.tolist().index("Kool"))

selected_value = st.sidebar.text_input('Enter Value', "Hugo Treffneri Gümnaasium")
filtered_data = data[data[selected_column] == selected_value]

if len(columns) > 0 and not filtered_data.empty:
    st.subheader('Filtered Data')
    st.write(filtered_data[columns])

    st.subheader('Data Visualization')
    
    fig = px.bar(filtered_data, x='Koht', y='Kokku', text='Nimi', color='Nimi',
                 labels={'Kokku': 'Total Points', 'Koht': 'Place', 'Nimi': 'Name'},
                 title='Individual Students\' Scores by Place',
                 height=400)

    fig.update_layout(xaxis_title='Place', yaxis_title='Total Points')
    fig.update_traces(textposition='outside', width=0.8, marker=dict(line=dict(width=2)), selector=dict(mode='markers+text'), opacity=0.6)
    fig.update_traces(marker_line_width=0)

    st.plotly_chart(fig)

else:
    st.warning('No data to display.')
