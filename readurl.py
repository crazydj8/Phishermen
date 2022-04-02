import urllib.request 

req = urllib.request.urlopen("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
l = []
for line in req: 
    l.append(line.decode("utf-8").strip().lower())

print(l)
    
