import urllib.request, urllib.error, urllib.parse
import ssl
import xml.etree.cElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_102438.xml'
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)

counts = tree.findall('.//count')
sum = 0

for count in counts:
    sum += int(count.text)

print(sum)