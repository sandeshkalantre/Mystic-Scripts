import requests
import sys
import re

level = sys.argv[1]
url = str(sys.argv[2])
req = requests.get(url)
f = re.sub(r'[^a-z]','  ',req.text,flags=re.IGNORECASE)
f = f.strip().split()


f = [x for x in list(set(f)) if len(x) > 1]
print len(f)
#f = f[500:]
print len(f)
def fuck_mi(ans):
    while 1:
        cookies = {'__cfduid':'df8d8fa7fecb87b9af53341b886f8dba71449517719','PHPSESSID':'t59ok36s6p0ms1qd17mupncst4'}
        r = requests.post('http://moodi.org/mith/level' + level + '/level' + level + '.php', data = {"answer":ans},cookies=cookies)
        return r.url
    
count = 0
for word in f:
    r_url = fuck_mi(word)
    print count,r_url,word
    count += 1
    if "level" + str(int(level) + 1) in r_url:
        break

