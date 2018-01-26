import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_69243.json'
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
lst = list()
for item in info['comments']:
    find1 = int(item['count'])
    lst.append(find1)
a = sum(lst)
print(a)
