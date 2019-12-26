from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
import Twitter_creds as TC
from datetime import date
import pathlib
from pathlib import Path
import json

import os
import re

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

class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fectched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data): #takes in data that is collected from StreamListener

        try:
            mydict = {}
            data = ""
            Tweets_folder = Path("Twitter Results")
            if Tweets_folder.exists() == False:
                Tweets_folder.mkdir()
            cwd = os.getcwd()
            #print(re.sub("\"\w+\":","", raw_data))
            #print(raw_data[0].id)
            clean_data = re.sub("\"\w+\":","", raw_data).strip("\n")
            #header = "Date_Created,	ID,	ID_STR,	Tweet_text,	Source,	Truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str:null,	in_reply_to_screen_name,	user,	id_str,	Name,	Screen_name,	Location,	URL,	Description,	,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	retweeted_status,	id,	id_str,	text,	source,	truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str,	in_reply_to_screen_name,	user,	id_str,	name,	screen_name,	location,	url,	description,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	symbols,	favorited,	retweeted,	filter_level,	lang,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	name,	id,	id_str,	indices,	#VALUE!	symbols,	favorited,	retweeted,	filter_level,	lang,	timestamp_ms"
            header = 'Date_Created,ID,User_Name,Screen_Name,Tweet,Geo'
            with open(self.fectched_tweets_filename, "a") as tf:
                if tf.tell() == 0:
                    tf.write(header +"\n")
                data=""
                #tf.write(raw_data.replace("\"","").strip("{}\n"))
                #raw_data_temp = raw_data.strip("{}")
                #dict_ready_data = raw_data_temp
                mydict = json.loads(raw_data)
                #mydict = json.loads(raw_data_temp)
                #print(raw_data)
                #print(type(raw_data_temp))
                #print(mydict)
                #print(mydict.keys())
                #print(f"the user string is {mydict['user']}")
                #print(mydict['user']['id'])
                data = f"{mydict['created_at']},{mydict['user']['id']},{mydict['user']['name']},{mydict['user']['screen_name']},{mydict['text']},{mydict['geo']}"
                print(data)
                tf.write(data)
                #tf.write(clean_data.replace("\"","").strip("{}\n"))
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
    fetched_tweets_filename = f"{cwd}\\Twitter Results\\{fetched_tweets_filename_noext}_{date.today()}.csv"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    user_id = input("Enter a user id to that you would like output the tweets for.\n>>")
    tweet_count = int(input("\tHow many tweets do you want for that user?\n\t>>"))
    twitter_client = TwitterClient(user_id)
    print(twitter_client.get_user_timeline_tweets(tweet_count))
