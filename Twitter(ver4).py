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
        stream.filter(track=[hash_tag_list])


class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fectched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data): #takes in data that is collected from StreamListener
        global now
        global end_time
        start = datetime.now()
        if want_runtime.upper().find("Y") < 0:
            now = 0
            end_time = 1
        while now < end_time:
            now = datetime.now()

            #/////////////////////////////////////////////////////////////
            #???????????????????????????????
            #Add a line that subtracts now from the end time and tells you how long the program has left to run
            #/////////////////////////////////////////////////////////////
            try:
                Tweets_folder = Path("Twitter Results")
                if Tweets_folder.exists() == False:
                    Tweets_folder.mkdir()
                cwd = os.getcwd()
                header = f'Date_Created~]ID~]User_Name~]Screen_Name~]Tweet_Text~]Geo_lat~]Geo_long~]Location~]Lat~]Long~]City~]Country~]Start_time_{now}~]End_time_{end_time}'
                with open(self.fectched_tweets_filename, "a", encoding="utf-8") as tf:
                    if tf.tell() == 0:
                        tf.write(header +"\n")
                    mydict = json.loads(raw_data.strip(","))
                    tweet_text = mydict['text'].replace('\n','').replace('\r','').replace('\t',' ')
                    try:
                        geo_lat = mydict['geo']['coordinates'][0]
                        geo_long = mydict['geo']['coordinates'][1]
                        lat = mydict['coordinates']['coordinates'][0]
                        long = mydict['coordinates']['coordinates'][1]
                        city = mydict['place']['name']
                        country = mydict['place']['country']
                    except:
                        geo_lat = "None"
                        geo_long = "None"
                        lat = "None"
                        long = "None"
                        city = "None"
                        country = "None"

                    data = f"{mydict['created_at']}~]{mydict['user']['id']}~]{mydict['user']['name']}~]{mydict['user']['screen_name']}~]{tweet_text}~]{geo_lat}~]{geo_long}~]{mydict['user']['location']}~]{lat}~]{long}~]{city}~]{country}"
                    # /////////////////////////////////////////////////////////////
                    #only outputs when it finds a search term in the user location, need to add code to allow you to sele
                    #which output you want
                    # /////////////////////////////////////////////////////////////
                    # if mydict['user']['location'] in hash_tag_list.split(","):
                    #     tf.write(data + "\n")
                    if len(data) > 0:
                        tf.write(data + "\n")

            except BaseException as e:
                print("!" *20 + "\n", f"!!ERROR!! {e}")

            return True

        def on_error(self, status_code): #
            if status_code == 420:
                return False
            print(status_code)
        print("Program Complete")
        sys.exit()


#Set_Path_File()
if __name__ == "__main__":
    cwd = os.getcwd()
    Set_Path_File()
    want_delay = 0
    want_start_time = input("Would you like to set a start time for this program? (Y/N)\n>>")
    if want_start_time .upper().find("Y") >= 0:
        input_error = 1
        want_delay = 1
        while input_error == 1:
            start_time_input = input("Please enter the desired start time in 24hr format (HH:MM)\n>>")
            try:
                start_time = dt.time(int(start_time_input.split(":")[0]), int(start_time_input.split(":")[1]), 00)
                print(start_time)
                check_start = datetime.time(datetime.now())
            except:
                print('!'*40 +"ERROR" + '!'*40)
                print("You did not enter the start time in the correct format.\nTry again.\n")
                continue
            input_error = 0
    want_runtime = input("Would you like to set the run time for this program? (Y/N)\n>>")
    if want_runtime.upper().find("Y") >= 0:
        input_error = 1
        while input_error == 1:
            runtime_input = input("Enter your the number of hours you would this code to run for:\n\tExample:\n\t\t1 hour = 1\n\t\t30 minutes = .5\n\t\t1 week = 10080\n>>")
            try:
                runtime = float(runtime_input.replace(",",""))
                end_time = datetime.now() + dt.timedelta(hours=runtime)
                now = datetime.now()
            except:
                print('!'*40 +"ERROR" + '!'*40)
                print("Please enter only integers as the desired runtime.\nTry again.\n")
                continue
            input_error = 0
    hash_tag_list = input("Please enter your search terms\nBe sure to separate them with a comma(,).\n>>")
    fetched_tweets_filename_noext = input("What would you like to name your output file?\n>>")
    fetched_tweets_filename = f"{cwd}\\Twitter Results\\{fetched_tweets_filename_noext}_{date.today()}.txt"
    twitter_streamer = TwitterStreamer()
    if want_delay:
        while check_start < start_time:
            print(f"Program will start at about {start_time}.\nThe program will run for {runtime/60} minutes.")
            time.sleep(60)
            check_start = datetime.time(datetime.now())
            if want_start_time.upper().find("Y") >= 0:
                end_time = datetime.now() + dt.timedelta(hours=runtime)
                now = datetime.now()
    print("Program Running.")
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


    #//////////////////////////////////////////////////////
    #These lines of code will stream the Tweets of individual users, when needed. It will need to be
    #set up as a module so I can either call the code when wanted
    #Ideally, I will want to be able to feed a list of users into the code
    # //////////////////////////////////////////////////////

    #user_id = input("Enter a user id to that you would like output the tweets for.\n>>")
    #tweet_count = int(input("\tHow many tweets do you want for that user?\n\t>>"))
    #twitter_client = TwitterClient(user_id)
    #print(twitter_client.get_user_timeline_tweets(tweet_count))
