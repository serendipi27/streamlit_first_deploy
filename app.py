
import streamlit as st

# 페이지 선택
# page = st.sidebar.selectbox('Select your page', ['Home', 'Data Visualization', 'About'])
page = st.sidebar.radio('Select your page', ['Home', 'Data Visualization', 'About'])

if page == 'Home':
    st.title('Home Page')
    st.write('Welcome to the Home Page!')
elif page == 'Data Visualization':
    st.title('Data Visualization')
    st.write('Here you can see interactive charts and data insights.')
elif page == 'About':
    st.title('About')
    st.write('This is an app built with Streamlit to demonstrate multi-page functionality.')
