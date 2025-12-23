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

target_url = f"https://www.data.jma.go.jp/stats/etrn/view/hourly_s1.php?prec_no=61&block_no=47759&year=2024&month=1&day=1&view=p1"
res = requests.get(target_url)
soup = BeautifulSoup(res.text, "html.parser")
# pythonで操作できるように変換したデータから表の部分を取得
weather_table = soup.find("table", id="tablefix1")
table_rows = weather_table.find_all("tr")

# それぞれの行から「時」「降水量」「気温」「日照時間」を取得して
# 最初の2行はラベルが書かれている部分なのでスキップする。
for row in table_rows[2:]:
    cells = row.find_all("td")
    weather_entry = [
        TARGET_YEAR,
        TARGET_MONTH,
        current_day,
        cells[0].text,  # 1列目の時
        cells[3].text,  # 4列目の降水量
        cells[4].text,  # 5列目の気温
        cells[10].text, # 11列目の日照時間
    ]
    # 1行ずつ取得したデータ(`waather_entry`)を`weather_data`に追加(`append`関数)
    weather_data.append(weather_entry)

df = pd.DataFrame(weather_data)
display(df)
