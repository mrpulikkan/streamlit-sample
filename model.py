import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.pyplot import xlabel
from matplotlib import style
import matplotlib.pyplot as plt
import streamlit as st

st.title("WELCOME")
st.sidebar.header("Contact US")
st.sidebar.subheader("Dont try this 1")
st.sidebar.text("welcome@gmail.com")
st.sidebar.text("0123456789")


st.success("You Connection is safe")
# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
	st.success("Status is Active")
else:
	st.warning("Not Active Yet")


#Text Input
name = st.text_input("Enter your name",)
age = st.text_input("Enter your age")
gender =st.radio("Select your gender",('Male','Female'))
occupation = st.selectbox("Your Occupation",['Student','Data Scientist','Programmer','Doctor','Businessman'])

submit = st.button("Register")
if submit:
	st.write("Welcome",name)
	st.write("This is the model deployment of a Streamlit file on Heroku")
  
view_more=st.button("About You")
if view_more :
	st.write("Name : ",name)
	st.write("Age : ",age)
	st.write("Gender : ",gender)
	st.write("Occupation : ",occupation)

goto_data=st.button("Goto Data")
if goto_data:
	docs = pd.read_csv("mtcars.csv")
	new_data =docs.head(15)
	st.header("Table")
	st.table(new_data)

	st.header("Joint Plot")
	print(sns.barplot(x='cyl',y='gear',data=new_data))
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()

	st.header("Violin Plot")
	print(sns.violinplot(docs['qsec'],kde=False))
	st.pyplot()

	st.header("Joint Plot")
	print(sns.jointplot(x='cyl',y='hp',data=docs,kind='scatter'))
	st.pyplot()
	



# Balloons
st.balloons()



