import urllib.error


def time_chart():
    import streamlit as st
    import pandas as pd
    import altair as alt

    # @st.cache(allow_output_mutation=True)
    # def fetch_dates():
    #     df = pd.read_csv('./csv/CK_Reviews_Payoff_9-4-2021.csv',
    #                      usecols=['Date', 'Rating'])
    #     return df
    #     # df = df_loc.join(df_loc['location'].str.split(',', expand=True))

    # df_datetime = fetch_dates()

    df_datetime = []

    sidebar_data_src = st.sidebar.radio(
        " Data source", ['Payoff', 'SoFi', 'Upstart'], 0)
    if sidebar_data_src == 'Payoff':
        df_datetime = pd.read_csv(
            './csv/CK_Reviews_Payoff_9-4-2021.csv')
    if sidebar_data_src == 'Upstart':
        df_datetime = pd.read_csv(
            './csv/CK_Reviews_Upstart_9-7-2021.csv')
    if sidebar_data_src == 'SoFi':
        df_datetime = pd.read_csv(
            './csv/CK_Reviews_SoFi_9-7-2021.csv')

    df_datetime['Date'] = df_datetime['Date'].astype('datetime64')

    st.write('### Rating Distribution')
    rating_distribution = alt.Chart(df_datetime).mark_bar(size=20).encode(
        y="Rating",
        x="count(Rating)):Q",
        tooltip=['count(Rating):Q', 'Rating'],
        color='Rating'
    ).properties(
        height=500,
    )
    st.altair_chart(rating_distribution, True)

    st.write('### Total Trend by Month')
    month_of_year = alt.Chart(df_datetime).mark_bar().encode(
        x="yearmonth(Date):O",
        y="count(Rating)):Q",
        tooltip=['count(Date):Q', 'yearmonth(Date):O', 'Rating'],
        color='Rating'
    ).properties(
        height=500
    )
    st.altair_chart(month_of_year, True)
    # st.info('Why did this drop off by 40% since October?')

    st.write('### Month of Year')
    month_of_year = alt.Chart(df_datetime).mark_bar(opacity=.8).encode(
        x="month(Date):O",
        y="count(Rating):Q",
        tooltip=['count(Date):Q', 'month(Date):O'],
        color='Rating'
    ).properties(
        height=500
    )
    st.altair_chart(month_of_year, True)

    st.write('### Day of Week')
    day_of_week = alt.Chart(df_datetime).mark_bar(opacity=.8).encode(
        x="day(Date):O",
        y="count(Rating):Q",
        tooltip=['count(Date):Q', 'day(Date):O'],
        color='Rating'
    ).properties(
        height=500
    )
    st.altair_chart(day_of_week, True)

    # st.write('### Time of day')
    # hour_of_day = alt.Chart(df_datetime).mark_bar().encode(
    #     x="hours(Date):O",
    #     y="count(Rating):Q",
    #     tooltip=['count(Date):Q', 'hours(Date):O'],
    #     color='Rating'
    # ).properties(
    #     height=500
    # )
    # st.altair_chart(hour_of_day, True)
