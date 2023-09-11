import pygwalker as pyg

import pandas as pd

import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(
    page_title="Pygwalker和Streamlit集成",
    layout="wide"
)

st.title("Pygwalker和Streamlit集成")

df = pd.read_excel(r'C:\Users\Admin\Desktop\in/副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx')
pyg_html = pyg.walk(df, return_html=True)
components.html(pyg_html, height=1000, scrolling=True)