import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np

def load_accidents(file_name):
    data = pd.read_csv(file_name, dtype = {'lon': float, 'lat':float})
    data = data.dropna(subset=['lon', 'lat'])
    data = data[ (data['lon'] != 0) & (data['lat'] != 0) ]
    return data

st.title("Velo hacks")

file_name = 'accidents-velos.csv'

accidents = load_accidents(file_name)
st.map(accidents)


