n=input('enter your name')
empty=''
for i in range(len(n)):
    if n[i] not in empty:
        empty+=n[i]
        print(n[i],':',n.count(n[i]))