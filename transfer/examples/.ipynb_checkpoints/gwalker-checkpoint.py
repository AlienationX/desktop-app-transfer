import pandas as pd
import pygwalker as pyg

df = pd.read_excel(r'C:\Users\Admin\Desktop\in/副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx')
gwalker = pyg.walk(df)