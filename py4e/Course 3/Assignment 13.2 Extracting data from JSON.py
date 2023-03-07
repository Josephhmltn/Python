import urllib.request, urllib.parse, urllib.error
import ssl
import json

#Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Prompt for URL to parse for JSON data
#URL used: http://py4e-data.dr-chuck.net/comments_1765687.json
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print(info)
comments = info['comments']
print("Count:",len(comments))
#print(json.dumps(info,indent=2))
#print(comments)
sum = 0
for count in comments:
    #print(int(count["count"]))
    sum = sum + int(count["count"])
print("Sum:",sum)