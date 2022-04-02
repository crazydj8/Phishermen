with open('web1.txt') as f:
    r = f.readlines()
for i in range(len(r)):
    r[i] = r[i].strip()
print(r)

