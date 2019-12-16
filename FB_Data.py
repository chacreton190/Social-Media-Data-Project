import requests


token ="" # insert token here

me_url = "https://graph.facebook.com/v5.0/me?fields=id,name&access_token=" +token
friends_url ="https://graph.facebook.com/v5.0/me/friends&access_token=" +token
my_data = requests.get(me_url)
my_friends = requests.get(friends_url)
print(my_data.text)
print(my_friends.text)