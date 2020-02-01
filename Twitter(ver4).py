import datetime as dt
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



def Set_Path_File():
    Tweets_folder = Path("Twitter Results")
    if Tweets_folder.exists() == False:
        Tweets_folder.mkdir()


def Output_twitter_data_time():
    global now
    global end_time
    while now < end_time:
        now = datetime.now()
        print(f"this is now {now}, this is end_time {end_time}")
        try:
            Tweets_folder = Path("Twitter Results")
            if Tweets_folder.exists() == False:
                Tweets_folder.mkdir()
            cwd = os.getcwd()
            header = 'Date_Created~]ID~]User_Name~]Screen_Name~]Tweet_Text~]Geo_lat~]Geo_long~]Location~]Lat~]Long~]City~]Country'
            with open(self.fectched_tweets_filename, "a") as tf:
                if tf.tell() == 0:
                    tf.write(header + "\n")

                mydict = json.loads(raw_data.strip(","))
                tweet_text = mydict['text'].replace('\n', '').replace('\r', '').replace('\t', ' ').encode("utf-8")
                # print(tweet_text)
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
                # only outputs when it finds a search term in the user location, need to add code to allow you to sele
                # which output you want
                # if mydict['user']['location'] in hash_tag_list.split(","):
                #     tf.write(data + "\n")
                if len(data) > 0:
                    tf.write(data + "\n")

        except BaseException as e:
            print("!" * 20 + "\n", f"!!ERROR!! {e}")
        return True


###   Twitter authenticator

def Output_twitter_data():

    try:
        Tweets_folder = Path("Twitter Results")
        if Tweets_folder.exists() == False:
            Tweets_folder.mkdir()
        cwd = os.getcwd()
        header = 'Date_Created~]ID~]User_Name~]Screen_Name~]Tweet_Text~]Geo_lat~]Geo_long~]Location~]Lat~]Long~]City~]Country'
        with open(self.fectched_tweets_filename, "a") as tf:
            if tf.tell() == 0:
                tf.write(header + "\n")

            mydict = json.loads(raw_data.strip(","))
            tweet_text = mydict['text'].replace('\n', '').replace('\r', '').replace('\t', ' ').encode("utf-8")
            # print(tweet_text)
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
            # only outputs when it finds a search term in the user location, need to add code to allow you to sele
            # which output you want
            # if mydict['user']['location'] in hash_tag_list.split(","):
            #     tf.write(data + "\n")
            if len(data) > 0:
                tf.write(data + "\n")
    except BaseException as e:
        print("!" * 20 + "\n", f"!!ERROR!! {e}")
    return True

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
        while now < end_time:
            now = datetime.now()
            print(f"this is now {now}, this is end_time {end_time}")
            try:
                Tweets_folder = Path("Twitter Results")
                if Tweets_folder.exists() == False:
                    Tweets_folder.mkdir()
                cwd = os.getcwd()
                header = 'Date_Created~]ID~]User_Name~]Screen_Name~]Tweet_Text~]Geo_lat~]Geo_long~]Location~]Lat~]Long~]City~]Country'
                with open(self.fectched_tweets_filename, "a") as tf:
                    if tf.tell() == 0:
                        tf.write(header +"\n")

                    mydict = json.loads(raw_data.strip(","))
                    tweet_text = mydict['text'].replace('\n','').replace('\r','').replace('\t',' ').encode("utf-8")
                    #print(tweet_text)
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
                    #only outputs when it finds a search term in the user location, need to add code to allow you to sele
                    #which output you want
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
    want_runtime = input("Would you like to set the run time for this program? (Y/N)\n>>")
    if want_runtime.upper().find("Y") >= 0:
        input_error = 1
        while input_error == 1:
            runtime_input = input("Enter your the number of hours you would this code to run for:\n\tExample:\n\t\t1 hour = 1\n\t\t30 minutes = .5\n\t\t1 week = 10080\n>>")
            try:
                runtime = float(runtime_input.replace(",",""))
            except:
                print('!'*40 +"ERROR" + '!'*40)
                print("Please enter only integers as the desired runtime.\nTry again.\n")
                continue
            input_error = 0
    hash_tag_list = input("Please enter your search terms\nBe sure to separate them with a comma(,).\n>>")
    fetched_tweets_filename_noext = input("What would you like to name your output file?\n>>")
    fetched_tweets_filename = f"{cwd}\\Twitter Results\\{fetched_tweets_filename_noext}_{date.today()}.txt"
    twitter_streamer = TwitterStreamer()
    end_time = datetime.now() + dt.timedelta(hours=runtime)
    now = datetime.now()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


    #//////////////////////////////////////////////////////
    #These lines of code will stream the Tweets of individual users, when needed. It will need to be
    #set up as a module so I can either call the
    #user_id = input("Enter a user id to that you would like output the tweets for.\n>>")
    #tweet_count = int(input("\tHow many tweets do you want for that user?\n\t>>"))
    #twitter_client = TwitterClient(user_id)
    #print(twitter_client.get_user_timeline_tweets(tweet_count))
