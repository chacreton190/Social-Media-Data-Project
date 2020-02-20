import Twitter_creds as TC
import twitter
import json


outfile = open("test2.txt","w", encoding="utf-8")
api = twitter.Api(consumer_key=TC.CONSUMER_KEY,
                      consumer_secret=TC.CONSUMER_SECRET,
                      access_token_key=TC.ACCESS_TOKEN,
                      access_token_secret=TC.ACCESS_TOKEN_SECRET,
                      sleep_on_rate_limit=True)
hash_tag_list = input("Please enter your search terms\nBe sure to separate them with a comma(,).\n>>").split(",")
#results = api.GetSearch(raw_query="q=%40twitterapi")
#results = str(api.GetSearch(raw_query="q=(%EF%82%A7%09%E2%80%9CHIV%E2%80%9D%20OR%20%E2%80%9CHIV%2FAIDS%E2%80%9D%20OR%20%E2%80%9CHIV%20OR%20testing%E2%80%9D%20OR%20%E2%80%9CHIV%20OR%20medication%E2%80%9D%20OR%20%E2%80%9CAIDS%20OR%20test%E2%80%9D%20OR%20%E2%80%9CHIV%20OR%20test%E2%80%9D%20OR%20%E2%80%9CHIV%2B%E2%80%9D%20OR%20%E2%80%9CHIV(%2B)%E2%80%9D%20OR%20%E2%80%9Crapid-HIV%20OR%20test%E2%80%9D%20OR%20%E2%80%9Crapid%20OR%20HIV%20OR%20test%E2%80%9D%20OR%20%E2%80%9Cora-sure%E2%80%9D%20OR%20%E2%80%9Corasure%E2%80%9D%20OR%20%E2%80%9CAcquired%20OR%20Immune%20OR%20Deficiency%20OR%20Syndrome%E2%80%9D%20OR%20%E2%80%9CAcyclovir%E2%80%9D%20OR%20%E2%80%9CADAP%E2%80%9D%20OR%20%E2%80%9CKaposi%27s%20OR%20Sarcoma%E2%80%9D%20OR%20%E2%80%9CThrush%E2%80%9D)&src=typed_query"))
for terms in hash_tag_list:
    results = api.GetSearch(term=terms, count= 100, lang="en")
    #, since = 2020 - 2 - 15, until = 2020 - 2 - 16
    print(results)
    for t in results:
        tweets = [t.AsDict() for t in results]
        print(t)
        #print(t["text"], t["lang"])
    str_result = str(results)
    outfile.write(str_result +"\n")

