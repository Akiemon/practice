# Google　Colaboratoryを使い、ヤフーの見出しをスクレイピングして、csvで保存するコードです


import urllib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from google.colab import files

url = "https://www.yahoo.co.jp/"

# ユーザーエージェントの設定（ヤフーはアカウント設定しないと見れない設定？）
# uaに関してはGitHubに載せる関係で///にしております

# ua = '///'

req = urllib.request.Request(url, headers={'User-Agent': ua})

html = urllib.request.urlopen(req)

soup = BeautifulSoup(html, "html.parser")

columns = ["NAME", "URL"]
df = pd.DataFrame(columns = columns)
# 動作確認
# print(df)

tags = soup.find("ul", {"class": "emphasis"})
for tag in tags:
  name = tag.a.text
  url = tag.a.get("href")
  se = pd.Series([name, url], columns)
  df = df.append(se, columns)

# csvで保存（実行するとダウンロードしちゃうのでコメントアウトにしてます）
filename = "result.csv"
df.to_csv(filename, encoding = "utf-8")
# files.download(filename)