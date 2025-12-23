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
for current_day in range(1, DAYS_IN_MONTH + 1):
    target_url = f"https://www.data.jma.go.jp/stats/etrn/view/hourly_s1.php?prec_no=61&block_no=47759&year={TARGET_YEAR}&month={TARGET_MONTH}&day={current_day}&view=p1"
    res = requests.get(target_url)
    soup = BeautifulSoup(res.text, "html.parser")
    weather_table = soup.find("table", id="tablefix1")
    table_rows = weather_table.find_all("tr")

    # 最初の2行をスキップする
    for row in table_rows[2:]:
        cells = row.find_all("td")
        weather_entry = [
            TARGET_YEAR,
            TARGET_MONTH,
            current_day,
            cells[0].text,
            cells[3].text,  # 降水量
            cells[4].text,  # 気温
            cells[10].text,  # 日照時間
        ]
        weather_data.append(weather_entry)

df = pd.DataFrame(weather_data)
display(df)
