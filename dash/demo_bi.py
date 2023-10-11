import pandas as pd
import streamlit as st

# 设置网页名称
st.set_page_config(page_title='调查结果')
# 设置网页标题
st.header('2020年调查问卷')
# 设置网页子标题
st.subheader('2020年各部门对生产部的评分情况')


df = pd.read_csv("../vgsales.csv")

# streamlit的多重选择(选项数据)
platform = df['Platform'].unique().tolist()
# streamlit的滑动条(年龄数据)
years = df['Year'].unique().tolist()


platform_selection = st.multiselect('平台:',
                                      platform,
                                      default=platform)

year_selection = st.slider('年份:',
                          min_value=min(years),
                          max_value=max(years),
                          value=(min(years), max(years)))


# 根据选择过滤数据
data = (df['Platform'].isin(platform_selection)) & (df['Year'].between(*year_selection))

# 绘制图形
import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
print(chart_data)

# 需要汇总后统计
# 根据选择分组数据
# df_grouped = df[mask].groupby(by=['评分']).count()[['年龄']]
# df_grouped = df_grouped.rename(columns={'年龄': '计数'})
# df_grouped = df_grouped.reset_index()

data_grouped = None
chart_data = data.pivot(index="Year", columns="Platform", values="Global_Sales")
print(chart_data.head())
# st.line_chart(chart_data)

# 根据筛选条件, 得到有效数据
number_of_result = df[data].shape[0]
st.markdown(f'*有效数据: {number_of_result}*')

# 展示表格，index和column会默认固定
st.dataframe(df[data])