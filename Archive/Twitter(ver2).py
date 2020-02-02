from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Twitter_creds
from datetime import date
import pathlib
from pathlib import Path
import os

def Set_Path_File():
    Tweets_folder = Path("Twitter Results")
    if Tweets_folder.exists() == False:
        Tweets_folder.mkdir()


class TwitterStreamer():
    #Class for streaming and processing live tweets
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list): #
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(Twitter_creds.CONSUMER_KEY, Twitter_creds.CONSUMER_SECRET)
        auth.set_access_token(Twitter_creds.ACCESS_TOKEN, Twitter_creds.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        # Need to add an option to pass in the search terms as an input from the user
        stream.filter(track=[hash_tag_list])

class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fectched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data): #takes in data that is collected from StreamListener
        try:
            Tweets_folder = Path("Twitter Results")
            if Tweets_folder.exists() == False:
                Tweets_folder.mkdir()
            cwd = os.getcwd()
            print(raw_data)
            header = "Date_Created,	ID,	ID_STR,	Tweet_text,	Source,	Truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str:null,	in_reply_to_screen_name,	user,	id_str,	Name,	Screen_name,	Location,	URL,	Description,	,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	retweeted_status,	id,	id_str,	text,	source,	truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str,	in_reply_to_screen_name,	user,	id_str,	name,	screen_name,	location,	url,	description,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	symbols,	favorited,	retweeted,	filter_level,	lang,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	name,	id,	id_str,	indices,	#VALUE!	symbols,	favorited,	retweeted,	filter_level,	lang,	timestamp_ms"
            with open(self.fectched_tweets_filename, "a") as tf:
                if tf.tell() == 0:
                    tf.write(header)
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #Need to fix output formatting the columns are not matching up
                tf.write(raw_data.replace("\"","").strip("{}\n"))
        except BaseException as e:
            print("!" *20 + "\n", f"!!ERROR!! {e}")
        return True

    def on_error(self, status_code): #
        print(status_code)

#Set_Path_File()
if __name__ == "__main__":
    cwd = os.getcwd()
    Set_Path_File()
    hash_tag_list = input("Please enter your search terms\nBe sure to separate them with a comma(,).\n>>")
    fetched_tweets_filename_noext = input("What would you like to name your output file?")
    fetched_tweets_filename = f"{cwd}\\Twitter Results\\{fetched_tweets_filename_noext}_{date.today()}.csv"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
