from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Twitter_creds
from datetime import date
import pathlib
from pathlib import Path
import os

Tweets_folder = Path("Twitter Results")
if Tweets_folder.exists() == False:
    Tweets_folder.mkdir()
cwd = os.getcwd()
outfile = open(cwd + f"\\Twitter Results\\Tweets{date.today()}.csv", "w")
header = "Date_Created,	ID,	ID_STR,	Tweet_text,	Source,	Truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str:null,	in_reply_to_screen_name,	user,	id_str,	Name,	Screen_name,	Location,	URL,	Description,	,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	retweeted_status,	id,	id_str,	text,	source,	truncated,	in_reply_to_status_id,	in_reply_to_status_id_str,	in_reply_to_user_id,	in_reply_to_user_id_str,	in_reply_to_screen_name,	user,	id_str,	name,	screen_name,	location,	url,	description,	translator_type,	protected,	verified,	followers_count,	friends_count,	listed_count,	favourites_count,	statuses_count,	created_at,	utc_offset,	time_zone,	geo_enabled,	lang,	contributors_enabled,	is_translator,	profile_background_color,	profile_background_image_url,	profile_background_image_url_https,	profile_background_tile,	profile_link_color,	profile_sidebar_border_color,	profile_sidebar_fill_color,	profile_text_color,	profile_use_background_image,	profile_image_url,	profile_image_url_https,	profile_banner_url,	default_profile,	default_profile_image,	following,	follow_request_sent,	notifications,	geo,	coordinates,	place,	contributors,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	symbols,	favorited,	retweeted,	filter_level,	lang,	is_quote_status,	quote_count,	reply_count,	retweet_count,	favorite_count,	entities,	urls,	user_mentions,	name,	id,	id_str,	indices,	#VALUE!	symbols,	favorited,	retweeted,	filter_level,	lang,	timestamp_ms"
outfile.write(header + "\n")
class StdOutListener(StreamListener):
    def on_data(self, raw_data): #takes in data that is collected from StreamListener
        global outfile
        # Add a line that strips out everything that comes before the ":" in the printout
        outfile.write(raw_data.replace("\"","").strip("{}").strip("\n"))
        print(raw_data.replace("\"","").strip("{}\n"))
        #print(type(raw_data))
        return True

    def on_error(self, status_code): #
        print(status_code)


if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(Twitter_creds.CONSUMER_KEY, Twitter_creds.CONSUMER_SECRET)
    auth.set_access_token(Twitter_creds.ACCESS_TOKEN, Twitter_creds.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)
# Need to add an option to pass in the search terms as an input from the user
    stream.filter(track=["drunk", "Weed",])


