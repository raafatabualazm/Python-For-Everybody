import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_102436.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

for tag in tags:
    num = int(tag.contents[0])
    sum += num

print(sum)
