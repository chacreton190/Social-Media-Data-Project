from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import Twitter_creds

class StdOutListener(StreamListener):
    def on_data(self, raw_data): #takes in data that is collected from StreamListener
        print(raw_data)
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
