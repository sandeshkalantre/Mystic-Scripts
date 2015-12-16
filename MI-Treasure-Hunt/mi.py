import requests
import sys
import re

level = sys.argv[1]
def fuck_mi(ans):
    while 1:
        cookies = {'__cfduid':'df8d8fa7fecb87b9af53341b886f8dba71449517719','PHPSESSID':'t59ok36s6p0ms1qd17mupncst4'}
        r = requests.post('http://moodi.org/mith/level' + str(level) + '/level' + str(level) + '.php', data = {"answer":ans},cookies=cookies)
        return r
r = fuck_mi("hint")
print r.text

