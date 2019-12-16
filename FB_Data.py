import requests


token ="EAAGujvXaMK8BABet9CEQAM0Mhy3bxRZAxplrxmpevrZBSxc1B8Or2UEfxn6HqTNIdcwvCmYPErFVGuOwizfJabFOhC5cRwKCCW3rV6lBZBIMM8dQsGGCfZBXIRco69jzeZCV4RDOjXiBmm9ZAoiazoJVE1Kd0L3UbAhrOqnogrHBepuztnlYAEJd8smd543rKNU7a0EMmiXgZDZD"

me_url = "https://graph.facebook.com/v5.0/me?fields=id,name&access_token=" +token
friends_url ="https://graph.facebook.com/v5.0/me/friends&access_token=" +token
my_data = requests.get(me_url)
my_friends = requests.get(friends_url)
print(my_data.text)
print(my_friends.text)