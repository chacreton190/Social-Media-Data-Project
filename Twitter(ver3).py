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
from datetime import datetime
import sys

start = datetime.time(datetime.now()).minute

def Set_Path_File():
    Tweets_folder = Path("Twitter Results")
    if Tweets_folder.exists() == False:
        Tweets_folder.mkdir()


###   Twitter authenticator
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(TC.CONSUMER_KEY, TC.CONSUMER_SECRET)
        auth.set_access_token(TC.ACCESS_TOKEN, TC.ACCESS_TOKEN_SECRET)
        return auth


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets= []

        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class TwitterStreamer():
    #Class for streaming and processing live tweets
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list): #
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        # Need to add an option to pass in the search terms as an input from the user
        stream.filter(track=[hash_tag_list])

        #global start


class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fectched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data): #takes in data that is collected from StreamListener
        global start
        try:
            Tweets_folder = Path("Twitter Results")
            if Tweets_folder.exists() == False:
                Tweets_folder.mkdir()
            cwd = os.getcwd()
            header = 'Date_Created~ID,User_Name~Screen_Name~Tweet~Geo'
            with open(self.fectched_tweets_filename, "a") as tf:
                if tf.tell() == 0:
                    tf.write(header +"\n")
                #////////////////////////////////////////////////////
                #still need to clean the output up need to figure out how to stop printing the blank lines

                mydict = json.loads(raw_data.strip(","))

                data = f"{mydict['created_at']}~{mydict['user']['id']}~{mydict['user']['name']}~{mydict['user']['screen_name']}~{mydict['text']}~{mydict['geo']}"
                print(data)

                if len(data) > 0:
                    tf.write(data + "\n")

        except BaseException as e:
            print("!" *20 + "\n", f"!!ERROR!! {e}")
        return True

    def on_error(self, status_code): #
        if status_code == 420:
            return False
        print(status_code)

#Set_Path_File()
if __name__ == "__main__":
    cwd = os.getcwd()
    Set_Path_File()
    hash_tag_list = input("Please enter your search terms\nBe sure to separate them with a comma(,).\n>>")
    #print(hash_tag_list)
    fetched_tweets_filename_noext = input("What would you like to name your output file?\n>>")
    fetched_tweets_filename = f"{cwd}\\Twitter Results\\{fetched_tweets_filename_noext}_{date.today()}.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

    #//////////////////////////////////////////////////////
    #These lines of code will stream the Tweets of individual users, when needed. It will need to be
    #set up as a module so I can either call the
    #user_id = input("Enter a user id to that you would like output the tweets for.\n>>")
    #tweet_count = int(input("\tHow many tweets do you want for that user?\n\t>>"))
    #twitter_client = TwitterClient(user_id)
    #print(twitter_client.get_user_timeline_tweets(tweet_count))
