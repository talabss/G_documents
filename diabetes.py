import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np


#read a csv file
#import csv file
#convert file to dataframe

df = pd.read_csv("diabetes.csv")
st.markdown("# first five iteams")
st.write(df.head())

st.markdown('# last ten items')
st.write(df.tall(10))

st.title("general information about diabetes analysis")
hall = df.describe
st.write(hall)

st.title('BloodPressure chart')
counted = df["BloodPressure"].value_counts().reset_index()
counted,columns = ["BloodPressure", "count"]
BloodPressure = px.pie(counted, names = "BloodPressure",values =
st.plotly_chart('BloodPressure', use_container_width = True)

#import -m pip install scikit-learn
#import -m pip install matlib
#download seaborn- python -m pip install seaborn


