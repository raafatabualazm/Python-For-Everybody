import urllib.request, urllib.parse, urllib.error
import ssl
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42
params = dict()
address = "Rochester Institute of Technology"
params['key'] = api_key
params['address'] = address
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = service_url + urllib.parse.urlencode(params)
conn = urllib.request.urlopen(url, context=ctx)
data = conn.read().decode()
j = json.loads(data)


print(j['results'][0]['place_id'])