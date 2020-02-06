import Twitter_creds as TC
import twitter
import json

outfile = open("test2.txt","w", encoding="utf-8")
api = twitter.Api(consumer_key=TC.CONSUMER_KEY,
                      consumer_secret=TC.CONSUMER_SECRET,
                      access_token_key=TC.ACCESS_TOKEN,
                      access_token_secret=TC.ACCESS_TOKEN_SECRET,
                      sleep_on_rate_limit=False,
                      chunk_size=500 * 1024)

results = str(api.GetSearch(raw_query="q=HIV HIV%2FAIDS&src=typed_query%20&result_type=recent&since=2014-07-19&count=900"))
f=","
str_result = str(results)
outfile.write(str_result)

