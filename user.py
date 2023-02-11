import requests
import re
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}
print("grab all users from wordpress site")
site = input("enter the site :")

resp = requests.get(site+'/wp-json/wp/v2/users/', headers=headers)
#
if 'name' in resp.text:
    users = re.findall('"name":"(.*?)",', resp.text)
    for user in users:
        print(user)
    else:
        print("can't find usernames sir:'/")
