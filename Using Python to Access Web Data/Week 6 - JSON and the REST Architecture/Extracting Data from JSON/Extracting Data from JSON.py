import urllib.request, urllib.parse, urllib.error
import ssl
import json

#url = input("Enter URL: ")
url = 'http://py4e-data.dr-chuck.net/comments_102439.json'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
j = json.loads(data)
sum = 0
for x in j['comments']:
    sum += int(x['count'])
print(sum)