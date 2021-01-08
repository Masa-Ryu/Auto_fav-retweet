import tweepy
import datetime


class twistream:
    """
    機能：
    ・検索
    ・TLツイートリツイート＆いいね
    ・トップアカウントのツイートリツイート＆いいね
    """
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
        self.Top_User = ''


    def search(self, keyword): #検索
        search_words = '({0}) -peing -com -jp -net'.format(keyword)
        count = 10
        search_results = self.api.search(q = search_words, lang = 'ja', result_type = 'recent', count = count, include_entities = True, tweet_mode = 'extended')
        return search_results


    def timeline(self): #タイムラインの取得
        return self.api.home_timeline()


    def top_user_timeline(self): #あるユーザーのタイムラインの取得
        return self.api.user_timeline(id = self.Top_User)


    def likes(self, tweets): #いいね！
        for tweet in tweets:
            tweet_id = tweet.id
            tweet_source = tweet.source
            if tweet_source == 'Twitter for iPhone':
                try:
                    self.api.create_favorite(tweet_id)
                except Exception as error:
                    print(error)
            elif tweet_source == 'Twitter for Android':
                try:
                    self.api.create_favorite(tweet_id)
                except Exception as error:
                    print(error)


    def retweets(self, tweets): #リツイート
        for tweet in tweets:
            tweet_id = tweet.id
            tweet_source = tweet.source
            if tweet_source == 'Twitter for iPhone':
                try:
                    self.api.retweet(tweet_id)
                except Exception as error:
                    print(error)
            elif tweet_source == 'Twitter for Android':
                try:
                    self.api.retweet(tweet_id)
                except Exception as error:
                    print(error)


    def likes_retweets(self, tweets): #いいね！とリツイート
        for tweet in tweets:
            tweet_id = tweet.id
            tweet_source = tweet.source
            if tweet_source == 'Twitter for iPhone':
                try:
                    self.api.retweet(tweet_id)
                    self.api.create_favorite(tweet_id)
                except Exception as error:
                    print(error)
            elif tweet_source == 'Twitter for Android':
                try:
                    self.api.retweet(tweet_id)
                    self.api.create_favorite(tweet_id)
                except Exception as error:
                    print(error)


    def get_timeline(self,tweets): #タイムラインの出力
        for tweet in tweets:
            contents = tweet.text
            try:
                print(contents)
            except Exception as error:
                print(error)