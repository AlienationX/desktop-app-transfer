import pandas as pd
import streamlit as st

# 设置网页名称，配置基本都是固定的，无法新增
st.set_page_config(
    page_title='调查结果',
    page_icon="🧊",
    # layout="wide",  # "centered" or "wide"
    # initial_sidebar_state="expanded",  # "auto", "expanded", or "collapsed"
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 设置网页标题
st.header('2020年调查问卷')
# 设置网页子标题
st.subheader('2020年各部门对生产部的评分情况')

# 数据读取
df = pd.read_csv("../vgsales.csv")
# 数据处理
df = df[df['Year'].notna()]  # 只保留Year不为空的数据， print(df[df['Year'].isna()])
df['Year'] = df['Year'].astype(int)  # 转换类型

# streamlit的多重选择(选项数据)
platform = df['Platform'].unique().tolist()
# streamlit的滑动条(年龄数据)
years = df['Year'].unique().tolist()
print(df)
print(platform)
print(years)


platform_selection = st.multiselect('平台：',
                                      platform,
                                      default=platform)

year_selection = st.slider('年份：',
                          min_value=min(years),
                          max_value=max(years),
                          value=(min(years), max(years)))


# 根据选择过滤数据
condition = (df['Platform'].isin(platform_selection)) & (df['Year'].between(*year_selection))

# 绘制图形
chart_data = df[condition].groupby(["Year", "Platform"], as_index=False).agg(
    Global_Sales = ("Global_Sales", "sum")
)
print(chart_data)
st.line_chart(chart_data, x="Year", y="Global_Sales", color="Platform")  # 多个维度的数据需要指明x和y

# 根据筛选条件, 得到有效数据
number_of_result = df[condition].shape[0]
st.markdown(f'**有效数据：{number_of_result}**')

# 展示表格，index和column会默认固定
st.dataframe(df[condition])
# table会全部加载数据，导致页面卡死
# st.table(df[condition])

# 官方示例
import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
print(chart_data)
st.subheader("Example")
st.text("官方示例：")
st.write("官方示例：")

tab1, tab2 = st.tabs(["📈 Chart", "⌨️ Data"])
# tab1.subheader("A tab with a chart")
tab1.line_chart(chart_data)  # 一个维度的数据可以直接使用
# tab2.subheader("A tab with a data")
tab2.dataframe(chart_data)

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)
print(chart_data)

with st.echo():
    st.write('This code will be printed')
    
st.info('This is a purely informational message', icon="ℹ️")

# 每个页面都需要增加?
# #MainMenu 是隐藏 右上角的...按钮
# footer 是隐藏 made with streamlit

# 隐藏made with streamlit
# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)