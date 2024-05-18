
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

df = px.data.experiment()

def bar_chart(df):
    bar_data = df.pivot_table(index='group', values='experiment_3', aggfunc='mean').reset_index()
    st.bar_chart(bar_data, x='group', y='experiment_3', color='group')

def box_chart(df):
    plt.figure(figsize=(10, 8))
    plt.title('Box plot of experiment_2 by gender')
    sns.boxplot(df, x='gender', y='experiment_2')
    st.pyplot(plt)

def violine_chart(df):
    plt.figure(figsize=(10, 8))
    plt.title('Violine plot of experiment_1 by gender')
    sns.violinplot(df, x='gender', y='experiment_1')
    st.pyplot(plt)

select_chart = st.selectbox("차트를 선택하세요", ['BarChart', 'BoxChart', 'ViolineChart'])

if select_chart == 'BarChart':
    bar_chart(df)
elif select_chart == 'BoxChart':
    box_chart(df)
else:
    violine_chart(df)
    
