import Twistream
from time import sleep
import csv


with open('AccessToken.csv') as f:#アクセストークンの読み込み
    reader = csv.reader(f)
    l = [row for row in reader]


keywords = [''] #検索ワード
keyword_index = 0 #インデックス数の初期化
i = 0
while i <= len(l):
    twistream = Twistream.twistream(
        consumer_key = '', #APIのコンスマーキー
        consumer_secret = '', #APIのシークレットコンスマーキー
        access_token = l[i][0],
        access_token_secret = l[i][1],
        )


    if keyword_index > len(keywords) - 1:
        keyword_index = 0


    else:
        twistream.likes_retweets(twistream.search(keywords[keyword_index]))
        keyword_index += 1


    sleep(3600)
    i += 1
    if i == len(l):
        i = 0