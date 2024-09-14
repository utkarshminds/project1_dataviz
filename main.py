import streamlit as st #python website
import pandas #reading data
st.title('My first python dataviz website') #title of website
upload_file = st.file_uploader('Upload a dataset', type=['csv']) #file uploader
if upload_file is not None: #if user selects file
    data = pandas.read_csv(upload_file) #first read it
    st.write(data) #display the file
    all_columns = data.columns.tolist() #get columns as python list
    selected_col = st.selectbox('Select a column', all_columns)#display dropdown menu
    if pandas.api.types.is_numeric_dtype(data[selected_col]): 
        #if column has numeric data
        st.write('Selected column', selected_col, "is numeric")
    else:
        #if column has nominal data (non-numeric data)
        st.write('Selected column', selected_col, "is nominal")




