import pygwalker as pyg

import pandas as pd

import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(
    page_title="Pygwalker和Streamlit集成",
    layout="wide"
)

st.title("Pygwalker和Streamlit集成")
df = pd.read_csv("../vgsales.csv")

pyg_html = pyg.walk(df, return_html=True)

components.html(pyg_html, height=1000, scrolling=True)