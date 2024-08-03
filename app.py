import streamlit as st

st.title("CampusX")

col1, col2 = st.columns(2)

with col1:
    st.image('img1.png')
with col2:
    st.write("""Welcome to CampusX, your go-to destination for mastering Data Science and Machine Learning! At CampusX, we offer expert-led courses with a focus on practical application, state-of-the-art labs, a vibrant community of innovators, and comprehensive career development support. Our courses cover foundational principles, machine learning, big data analytics, and deep learning specialization. Join us on a transformative journey where passion meets purpose, and education evolves into empowerment. Subscribe now to CampusX for a future reshaped by tech excellence! 🚀📈 #CampusX #DataScience #MachineLearning #TechExcellence""")

st.header('Courses Offered')
st.subheader('Data Science')
st.subheader('Data Analysis')
st.subheader('Data Engineering')
st.subheader('Python')
st.subheader('DBMS')