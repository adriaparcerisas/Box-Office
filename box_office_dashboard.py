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
st.set_page_config(page_title="American Box study", layout="wide",initial_sidebar_state="collapsed")
st.title('American Box study')


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
plt.figure(figsize=(10,5))
for column in top_grossing_movies.columns:
    plt.plot(top_grossing_movies[column])
plt.xlabel('Date')
plt.ylabel('Gross Revenue')
plt.title('Top Grossing Movies Over Time')
st.pyplot()

# Daily Gross Revenue Section
st.header("Daily Gross Revenue")
st.markdown("This section shows the daily gross revenue.")
daily_gross = data[['Date', 'Gross']]
daily_gross['Date'] = pd.to_datetime(daily_gross['Date'])
daily_gross.set_index('Date', inplace=True)
daily_gross = daily_gross.resample('D').sum().reset_index()
top_grossing_movies = top_grossing_movies.fillna(0)
daily_gross['Gross'] = daily_gross['Gross'].apply(pd.to_numeric, errors='coerce')
plt.figure(figsize=(10,5))
plt.plot(daily_gross['Date'], daily_gross['Gross'])
plt.xlabel('Date')
plt.ylabel('Gross Revenue')
plt.title('Daily Gross Revenue')
st.pyplot()

# Gross Revenue Comparison Section
st.header("Gross Revenue Comparison")
st.markdown("This section shows the percent change of gross revenue compared to the previous day.")
gross_revenue_comparison = data[['Date', '%± YD']]
gross_revenue_comparison['Date'] = pd.to_datetime(gross_revenue_comparison['Date'])
gross_revenue_comparison['%± YD'] = gross_revenue_comparison['%± YD'].apply(pd.to_numeric, errors='coerce')
plt.figure(figsize=(10,5))
plt.plot(gross_revenue_comparison['Date'], gross_revenue_comparison['%± YD'])
plt.xlabel('Date')
plt.ylabel('% Change in Gross Revenue')
plt.title('Gross Revenue Comparison')
st.pyplot()

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




