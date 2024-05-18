
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

df = px.data.experiment()
# df

plt.figure(figsize=(10, 8))
plt.title('Violine plot of experiment_1 by gender')
sns.violinplot(df, x='gender', y='experiment_1')
st.pyplot(plt)
