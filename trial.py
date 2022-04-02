import readurl as m

url = 'http://activate.facebook.fblogins.net/88adbao798283o8298398?login.asp'#input()
def method(url):
        d = url.split("://")
        d = d[1].split("/")
        d1 = d[0].split('.')
        return(d1)
        
tld = method(url)
def check(tld):
    for i in m.l:
        if i==tld:
            return True
    return False

if check(tld[-1]):
    print("legit")
else:
    print("Not legit")
