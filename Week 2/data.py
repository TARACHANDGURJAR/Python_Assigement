import re
fl = open('tara.txt')
x=0
for line in fl:
    y = re.findall('[0-9]+',line)
    if not y:
        continue
    else:
        for y1 in y:
            x += int(y1)
print(x)
