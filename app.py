import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

paris_depts = [91,92,75,77,93,94,95,78]

def load_accidents(file_name):
    data = pd.read_csv(file_name, dtype = {'lon': float, 'lat':float})
    data = data.dropna(subset=['lon', 'lat'])
    data = data[data['departement'].isin([str(dept) for dept in paris_depts])]
    data = data[data['lon'].between(2.1, 2.5)]
    data = data[data['lat'].between(48.75, 48.95)]

    return data

def get_age(row):
    x, y = map(int, row.split('-'))
    return (x+y)/2

st.title("Velo hacks")

file_name = 'accidents-velos.csv'

data_set = load_accidents(file_name)
st.map(data_set)

data_set['mean_age'] = data_set['age'].apply(get_age)
data_set = data_set[ data_set['mean_age'] < 100]
fig, ax = plt.subplots()
sns.histplot(data=data_set, x="mean_age", binwidth=1, ax=ax)

st.pyplot(fig)

fig2, ax = plt.subplots()
sns.countplot(x=data_set["sexe"])
st.pyplot(fig2)

fig3, ax = plt.subplots()
g = sns.countplot(x=data_set["gravite accident"])
g.set_xticklabels(g.get_xticklabels(), rotation=90)
st.pyplot(fig3)

fig4, ax = plt.subplots()
g = sns.countplot(x = data_set['motif deplacement'])
g.set_xticklabels(g.get_xticklabels(), rotation=90)
st.pyplot(fig4)

fig6, ax = plt.subplots()
sns.countplot(data=data_set, y="existence securite", hue="gravite accident")
st.pyplot(fig6)


fig7, ax = plt.subplots()
g = sns.countplot(x = data_set[ data_set['gravite accident'] == '3 - Tué' ]['existence securite'])
g.set_xticklabels(g.get_xticklabels(), rotation=90)
st.pyplot(fig7)