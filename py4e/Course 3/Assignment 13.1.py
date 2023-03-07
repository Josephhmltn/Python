import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

#Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Prompt for URL to parse for XML data
#URL used: http://py4e-data.dr-chuck.net/comments_1765686.xml
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print("Count:",len(counts))
sum = 0
for count in counts :
    count = int(count.text)
    #count = int(count)
    #print(type(count))
    sum = sum + count
print("Sum:",sum)