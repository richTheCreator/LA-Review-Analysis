import nltk
import streamlit as st


def nounchunks():

    from nltk.corpus import stopwords
    from collections import Counter
    from io import StringIO
    import pandas as pd
    import altair as alt

    alt.themes.enable('vox')

    df_nouns = []

    sidebar_data_src = st.sidebar.radio(
        " Data source", ['Payoff', 'SoFi', 'Upstart'], 0)
    if sidebar_data_src == 'Payoff':
        df_nouns = pd.read_csv(
            './csv/nounchunks_payoff.csv')
    if sidebar_data_src == 'Upstart':
        df_nouns = pd.read_csv(
            './csv/nounchunks_Upstart.csv')
    if sidebar_data_src == 'SoFi':
        df_nouns = pd.read_csv(
            './csv/nounchunks_SoFi.csv')
  

    st.write('### Noun test')
    noun_chart = alt.Chart(df_nouns).mark_bar(size=20).encode(
        x=alt.X('count', axis=alt.Axis(title='Counts')),
        y=alt.Y('Noun Chunk',
                sort=alt.EncodingSortField(
                    field='count', order='descending', op='sum'),
                axis=alt.Axis(title='Title')
                ),
        tooltip=['count'],
        color='Noun Chunk',
    ).configure_axis(
        labelFontSize=18,
        titleFontSize=20
    )
    st.altair_chart(noun_chart, True)


nounchunks()
