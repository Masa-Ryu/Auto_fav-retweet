import tweepy
import webbrowser
import csv


def get_access_token(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    webbrowser.open(auth.get_authorization_url())
    verifier = input('Verifier:')
    auth.get_access_token(verifier)


    print("Access Token:", auth.access_token)
    print("Access Token Secret:", auth.access_token_secret)
    print('アクセストークン取得成功')
    with open('AccessToken.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([auth.access_token, auth.access_token_secret])


get_access_token(
    consumer_key = '', #APIのコンスマーキー
    consumer_secret = '', #APIのシークレットコンスマーキー
)