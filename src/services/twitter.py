"""
  twitter.py
  ---------

  used to get tweets from Twitter

"""


from twython import Twython, TwythonError

"""
   method get_tweets - from Twitter using Twython
      args :
         key = twitter app key
         secret = twitter app secret
         screen_name = twitter screen name of the tweeter (w/o @ sign)
         tweet_count = number of tweets to retrieve
"""


def get_tweets(key, secret, screen_name, tweet_count):
    # use the twitter app key and app secret to get an access token
    twitter = Twython(key, secret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    #
    # use the access token to authorize our calls
    twitter = Twython(key, access_token=ACCESS_TOKEN)
    #
    # get tweets for this screen_name - only get # specified in tweet_count
    try:
        user_timeline = twitter.get_user_timeline(screen_name=screen_name,
                                                  count=tweet_count)
        # convert tweets to utf-8
        user_tweets = []
        for tweet in user_timeline:
            converted_tweet = tweet['text'].encode('utf-8')
            user_tweets.append(converted_tweet)
        return user_tweets
    #error
    except TwythonError:
        # don't send anything back - maybe log error?
        return None
