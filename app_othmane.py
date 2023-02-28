import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder


def load_accidents(file_name):
    data = pd.read_csv(file_name, dtype={"lon": float, "lat": float})
    data = data.dropna(subset=["lon", "lat"])
    data = data[(data["lon"] != 0) & (data["lat"] != 0)]
    return data


st.title("Velo hacks")

file_name = "accidents-velos.csv"

accidents = load_accidents(file_name)

st.map(accidents)


def process_data(data, date_col):
    data[date_col] = pd.to_datetime(data[date_col])
    return data


def get_age(data):
    def process_age(x):
        try:
            return float(x.split("-")[0])
        except:
            return x

    data["age_min"] = data["age"].apply(process_age)
    return data


def get_proppreprocess_date(
    numeric_features,
    categorical_features,
    ordinal_features,
):
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    ordinal_transformer = Pipeline(
        steps=[
            ("encoder", OrdinalEncoder()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
            ("ord", ordinal_transformer, ordinal_features),
        ]
    )
    return preprocessor


with st.expander("Othmane non supervised clustering"):
    accidents = process_data(accidents, "date")
    label = "gravite accident"

    columns_to_use = [
        "departement",
        "lat",
        "heure",
        "usage securite",
        "luminosite",
        "circulation",
        "commune",
        "lon",
        "conditions atmosperiques",
        "sexe",
        "age",
    ] + [label]

    df = accidents[columns_to_use].copy()
    df = get_age(df)

    num_columns = ["lat", "age_min", "heure", "lon"]
    ordinary_columns = [
        "sexe",
        "luminosite",
        "circulation",
        "conditions atmosperiques",
        "usage securite",
    ]
    cat_columns = [
        "departement",
        "commune",
    ]

    for col in ordinary_columns + cat_columns:
        st.write(col)
        st.dataframe(df[col].value_counts())

    for col in num_columns:
        st.write(col)
        st.dataframe(df[[col]].describe())

    st.dataframe(df)
    st.write("columns", df.columns.tolist())
    st.write("number of columns", df.shape[1])
    st.write("Number of accidents ", df.shape[0])
