import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#URL used: http://py4e-data.dr-chuck.net/known_by_Raine.html
url = input("Enter URL: ")
#if (len(url)) < 1 :
#    url = "http://py4e-data.dr-chuck.net/known_by_Raine.html"
count = int(input("Enter count: "))
position = int(input("Enter position: "))

#Construct list of names from each URL link follow
names = list()
while count > 0 :
    print ("Retrieving: ",url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tag = soup('a')
    name = tag[position-1]
    names.append(name.contents[0])
    url = tag[position-1]['href']
    count = count - 1
#Print last item in the list
print (names[-1])