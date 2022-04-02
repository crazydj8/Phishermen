import Modulo_phish as m

url =  'http://activate.facebook.fblogins.net/88adbao798283o8298398?login.asp'#input()
def method(url):
        if url[0:5]=='http:':
            url = url[7:len(url)]
        elif url[0:5]=='https':
            url = url[8:len(url)]
        url = url.split('/')
        url_1 = url[0].split('.')
        tld = url_1[-1]
        return tld
tld = method(url)
def check(tld):
    for i in m.l:
        if i==tld:
            return True
    return False
if check(tld):
    print("legit")
else:
    print("Not legit")