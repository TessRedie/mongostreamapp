
import streamlit as st
import pandas as pd



# streamlit_app.py

import streamlit as st
import pymongo

#Connect to the server MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')


#create DB named 'MTSpam'
#db = client['Iris']



db = client["streamlipro"]
mycollection = db['iris']
st.write(mycollection)
all_records = mycollection.find()
for row in all_records:
    st.write(row)
