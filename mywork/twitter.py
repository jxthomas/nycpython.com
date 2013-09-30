import os
from twython import Twython,TwythonError

#
#  function to get tweets from Twitter using Twython
#

def get_tweets (key,secret,screen_name,tweet_count):

    #
    # use our twitter app key and app secret to get an access token
    #

    twitter = Twython(key,secret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    
    #
    # use the access token to authorize our calls
    #
    twitter = Twython(key, access_token=ACCESS_TOKEN)

    #
    # get tweets for this screen_name - only get # specified in tweet_count
    #
    try:
        user_timeline = twitter.get_user_timeline(screen_name=screen_name,count=tweet_count)
        return user_timeline
    
    except TwythonError as e:
        # don't see anything back
        print (e)
        return Nothing

#
# main - call get_tweets
#

if __name__ == '__main__':
    
    ## get keys from the environment
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

    # make the call
    #nycpython @nycpythonmeetup
    tweets = get_tweets(CONSUMER_KEY,CONSUMER_SECRET,'nycpythonmeetup',3)
    
    # print the tweets
    for tweet in tweets:
        print (tweet['text'].encode('utf-8'))
        print('-----------------------------')


