import pandas as pd
# import qgrid
from pivottablejs import pivot_ui
# from pandasgui import show
import tabloo
import dtale

df = pd.read_csv("vgsales.csv")

dtale.show(df)