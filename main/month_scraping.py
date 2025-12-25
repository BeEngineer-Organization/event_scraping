import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

TARGET_YEAR = 2024
TARGET_MONTH = 1
# 1月31日が1月の最終日
DAYS_IN_MONTH = 31

weather_data = [["年", "月", "日", "時間", "降水量", "気温", "日照時間"]]

#1月1日から1月31日で`day`の部分を変更して繰り返しアクセス

df = pd.DataFrame(weather_data)
display(df)
