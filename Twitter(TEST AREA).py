import datetime as dt
from datetime import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import Twitter_creds as TC
from datetime import date
from pathlib import Path
import json
import os
import sys
import time
import tweepy



###   Twitter authenticator
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(TC.CONSUMER_KEY, TC.CONSUMER_SECRET)
        auth.set_access_token(TC.ACCESS_TOKEN, TC.ACCESS_TOKEN_SECRET)
        return auth

# CONSUMER_KEY = TC.CONSUMER_KEY
# CONSUMER_SECRET = TC.CONSUMER_SECRET
# ACCESS_TOKEN = TC.ACCESS_TOKEN
# ACCESS_TOKEN_SECRET = TC.ACCESS_TOKEN_SECRET

# logger = logging.getLogger()





class TwitterClient():
    def create_auth():
        # consumer_key = os.getenv(CONSUMER_KEY)
        # consumer_secret = os.getenv(CONSUMER_SECRET)
        # access_token = os.getenv(ACCESS_TOKEN)
        # access_token_secret = os.getenv(ACCESS_TOKEN_SECRET)
        CONSUMER_KEY = TC.CONSUMER_KEY
        CONSUMER_SECRET = TC.CONSUMER_SECRET
        ACCESS_TOKEN = TC.ACCESS_TOKEN
        ACCESS_TOKEN_SECRET = TC.ACCESS_TOKEN_SECRET
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


    def __init__(self, twitter_user=None):
        TwitterAuthenticator() = create_auth()
        self.auth = TwitterAuthenticator()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

        f = tweepy.API(auth_handler=auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
        # api = tweepy.API(auth, wait_on_rate_limit=True,
        #          wait_on_rate_limit_notify=True)
        print(type(f))
       # api object is being used to talk to twitter
        try:
            f.verify_credentials()
        except Exception as e:
            # logger.error("Error creating API", exc_info=True)
            raise e
        # logger.info("API created")
        return f


API = TwitterClient()
API.update_status('Hello World!')