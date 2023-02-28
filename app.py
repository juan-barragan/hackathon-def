import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np

arr = np.random.normal(1, 1, size=100)

st.title("Velo hacks")

df = pd.read_csv("accidents-velos.csv")


st.dataframe(data=df.head(10))
