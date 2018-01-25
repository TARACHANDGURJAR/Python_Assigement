import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_69242.xml'
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
lst = list()
for item in results:
    find1 = int(item.find('count').text)
    lst.append(find1)
a = sum(lst)
print(a)
