#!/usr/bin/env python
# coding: utf-8

# In[49]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
import altair as alt
from datetime import datetime
import statistics as stats
st.set_option('deprecation.showPyplotGlobalUse', False)


# Load data from excel file
data = pd.read_excel("box_office_data.xlsx")
#data['Date'] = pd.to_datetime(data['Date'])

# Introduction
st.title("American Box Office Dashboard")
st.markdown("The American Box Office is the measurement of the performance of movies in theaters across the United States and Canada. This dashboard will explore the top grossing movies, their releases, and their performance over time. Let's get started!")

# Top 10 Movies Section
#st.header("Top 10 Movies")
#st.markdown("This section shows the top 10 movies by gross revenue.")
#top_10 = data[['#1 Release', 'Gross']].groupby('#1 Release').sum().sort_values(by=['Gross'], ascending=False).head(10)
#st.write(top_10)

# Top Grossing Movies Over Time Section
st.header("Top Grossing Movies Over Time")
st.markdown("This section shows the top grossing movies over time.")
top_grossing_movies = data.pivot(index='Date', columns='#1 Release', values='Gross')
top_grossing_movies = top_grossing_movies.fillna(0)
top_grossing_movies = top_grossing_movies.apply(pd.to_numeric, errors='coerce')
top_grossing_movies = top_grossing_movies.reset_index().melt('Date', var_name='Movie', value_name='Gross')
chart = alt.Chart(top_grossing_movies).mark_line().encode(
    x='Date:T',
    y=alt.Y('Gross:Q', axis=alt.Axis(format='$')),
    color='Movie:N'
).properties(
    width=800,
    height=400,
    title='Top Grossing Movies Over Time'
)
st.altair_chart(chart)

# Daily Gross Revenue Section
st.header("Daily Gross Revenue")
st.markdown("This section shows the daily gross revenue.")
daily_gross = data[['Date', 'Gross']]
daily_gross['Date'] = pd.to_datetime(daily_gross['Date'])
daily_gross = daily_gross.groupby('Date')['Gross'].sum().reset_index()
daily_gross['Gross'] = daily_gross['Gross'].fillna(0)
daily_gross['Gross'] = daily_gross['Gross'].apply(pd.to_numeric, errors='coerce')
chart = alt.Chart(daily_gross).mark_line().encode(
    x='Date:T',
    y=alt.Y('Gross:Q', axis=alt.Axis(format='$')),
).properties(
    width=800,
    height=400,
    title='Daily Gross Revenue'
)
st.altair_chart(chart)


# Gross Revenue Comparison Section
st.header("Gross Revenue Comparison Year-toDate")
st.markdown("This section shows the percent change of gross revenue compared year-to-date.")
gross_revenue_comparison = data[['Date', '± YD']]
gross_revenue_comparison['Date'] = pd.to_datetime(gross_revenue_comparison['Date'])
gross_revenue_comparison['Date'] = gross_revenue_comparison['Date'].fillna(0)
gross_revenue_comparison['± YD'] = gross_revenue_comparison['± YD'].apply(pd.to_numeric, errors='coerce')
chart = alt.Chart(gross_revenue_comparison).mark_line().encode(
    x='Date:T',
    y=alt.Y('± YD:Q', axis=alt.Axis(format='$')),
).properties(
    width=800,
    height=400,
    title='Gross Revenue Comparison Year-to-Date'
)
st.altair_chart(chart)

# Gross Revenue Comparison Section 2
st.header("Gross Revenue Last Week Comparison")
st.markdown("This section shows the percent change of gross revenue compared to the previous week.")
gross_revenue_comparison = data[['Date', '± LW']]
gross_revenue_comparison['Date'] = pd.to_datetime(gross_revenue_comparison['Date'])
gross_revenue_comparison['Date'] = gross_revenue_comparison['Date'].fillna(0)
gross_revenue_comparison['± LW'] = gross_revenue_comparison['± LW'].apply(pd.to_numeric, errors='coerce')
chart = alt.Chart(gross_revenue_comparison).mark_line().encode(
    x='Date:T',
    y=alt.Y('± LW:Q', axis=alt.Axis(format='$')),
).properties(
    width=800,
    height=400,
    title='Gross Revenue Comparison over the last week'
)
st.altair_chart(chart)

# Add line chart of top 10 gross over time
plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["Top 10 Gross"], marker="o", color="blue")
plt.title("Top 10 Gross at American Box Office")
plt.xlabel("Date")
plt.ylabel("Top 10 Gross")
st.pyplot()

# Add bar chart of number of releases by day
plt.figure(figsize=(10, 6))
plt.bar(data["Day"], data["Releases"], color="green")
plt.title("Number of Releases by Day")
plt.xlabel("Day")
plt.ylabel("Number of Releases")
st.pyplot()


# Add table of top 10 grossing movies
st.markdown("## Top 10 Grossing Movies")
st.table(data[["#1 Release", "Gross"]][:10])


# In[50]:


st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/Box-Office)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:




