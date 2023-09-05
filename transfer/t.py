import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_excel(r"C:\Users\Admin\Desktop\in\副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx")
# df = pd.read_excel(r"C:\Users\Admin\Desktop\in\1.xlsx")
profile = ProfileReport(df, title="Report", minimal=True)
profile.to_file("output_file.html")