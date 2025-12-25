import requests
from bs4 import BeautifulSoup
# 取得したデータを表示しやすくするためのパッケージ
import pandas as pd
# 取得したデータを表示するためのパッケージ
from IPython.display import display

# 取得したデータを格納するためのリスト
weather_data = [["年", "月", "日", "時間", "降水量", "気温", "日照時間"]]

# 取得する日付の情報
TARGET_YEAR = 2024
TARGET_MONTH = 1
current_day = 1

target_url = f""
# res = 
# soup = BeautifulSoup(res.text, "html.parser")
# pythonで操作できるように変換したデータから表の部分を取得
# weather_table = 
# table_rows = 

# それぞれの行から「時」「降水量」「気温」「日照時間」を取得して
# 最初の2行はラベルが書かれている部分なのでスキップする。
# for文スタート
    # cells = 
    # weather_entry = [
    #     TARGET_YEAR,
    #     TARGET_MONTH,
    #     current_day,
    #     # 1列目の時
    #     # 4列目の降水量
    #     # 5列目の気温
    #     # 11列目の日照時間
    # ]
    # 1行ずつ取得したデータ(`waather_entry`)を`weather_data`に追加(`append`関数)
    # weather_data.append(weather_entry)

df = pd.DataFrame(weather_data)
display(df)
