# 1. [requests]自動でwebサイトにアクセスするために使うパッケージ
import requests
# 2. [bs4]webサイトから取得したデータをpythonで扱える形式に変換するためのパッケージ
from bs4 import BeautifulSoup

# 3. アクセスするページのURL
target_url = "https://www.digital.go.jp/"

# 4.ページにアクセス
res = requests.get(target_url)

# 5. pythonで扱えるように取得したデータを変換
data = BeautifulSoup(res.text, "html.parser")

# 6.`span`タグでclass名が`attention-item__text--isInformation`であるタグ(部分)を取り出す。
important_news = data.find("span",class_="attention-item__text--isInformation")

# 7. タグ内の文章を表示する
print(important_news.text)
