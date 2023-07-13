#Streamlit example
import streamlit as st
#st.set_page_config(page_title="My streamliting",page_icon='C:\Users\acer\Mypython\flowers.jpg')
st.set_page_config(page_title='My streamliting',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fill Form','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title("Onlei Technologies")
st.header("By Abhinav Srivastava Sir")
st.text("This is a tutorial on streamlit library. Created 13 July 2023")

if(mymenu=='Home'):
    st.markdown("<center><h1>WELCOME!!! </h1></center>", unsafe_allow_html=True)
    st.video("https://youtu.be/Zzg5QX5Ul64")
elif(mymenu=='Fill Form'):
    with st.form('MyForm'):
        name=st.text_input(' Enter Name')
        dob=st.date_input('Choose Date of Birth')
        marks=st.slider('Choose Marks')
        k=st.form_submit_button('Submit Form')
        if k:
           st.write('name= ',name,'dob= ',dob,'marks= ',marks)
elif(mymenu=="Downloads"):
    st.header("Downloads")
    st.download_button("Download Now","Hello this is the downloaded data","onlei.txt")
#    st.download_button("DownloadNow",'C:/Users/acer/Mypython/greenrose.jpg')