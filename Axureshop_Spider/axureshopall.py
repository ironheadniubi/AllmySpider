import re
import requests
url = "https://www.axureshop.com/a"
response = requests.get(url)
#print(response.text)
uid = re.findall(r'https://www.axureshop.com/a/(\d+).html',response.text)
uid = (list(set(uid)))
#http://demo.axureshop.com/?url=http://cloud.axureshop.com/a59d0k&buyurl=https://www.axureshop.com/a/1170349.html
ulrs = "https://www.axureshop.com/a/1170349.html"
response = requests.get(ulrs)

ur = re.findall(r'http://demo.axureshop.com/.url=http://cloud.axureshop.com/.*?&buyurl=https://www.axureshop.com/a/.*?.html',response.text)