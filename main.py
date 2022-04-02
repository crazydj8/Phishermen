from nicedomains import nicedomains
from readurl import top
import extender

link = input("Enter your link:")
link = extender.extend(link)

def check(url):
    d = url.split("://")[1]
    d = d.split("/")[0]
    if "@" in d:
        x = d.index("@")
        d = d[x+1:]
    d1 = d.split('.')
    return(d1)

x = check(link)
condition = 1
if x[-1] not in top:
    condition = 0
if x[-2] not in nicedomains:
    condition = 0
if condition == 0:
    print("invalid")
else:
    print("Valid")

