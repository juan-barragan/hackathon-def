import streamlit as st
import pandas as pd
import numpy as np

paris_depts = [91,92,75,77,93,94,95,78]

def load_accidents(file_name):
    data = pd.read_csv(file_name, dtype = {'lon': float, 'lat':float})
    data = data.dropna(subset=['lon', 'lat'])
    data = data[data['departement'].isin([str(dept) for dept in paris_depts])]
    data = data[data['lon'].between(2.1, 2.5)]
    data = data[data['lat'].between(48.75, 48.95)]

    return data

st.title("Velo hacks")

file_name = 'accidents-velos.csv'

accidents = load_accidents(file_name)
st.map(accidents)




