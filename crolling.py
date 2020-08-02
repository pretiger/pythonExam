import urllib.request as req
import re
res = req.urlopen('http://daum.net')
data = res.read().decode('utf-8')
result = re.findall('https://[./-_\w]+.jpg', data)
for link in result:
    idx = link.rfind('/')
    with open(link[idx+1:], 'wb') as f:
        pic = req.urlopen(link)
        f.write(pic.read())
