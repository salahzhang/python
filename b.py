def tidy():
    n=input().strip()
    if len(n)==1:
        return n

    i=0
    peak=0
    while i<len(n)-1:
        if n[i]>n[i+1]:
            break
        elif n[i]==n[i+1]:
            i+=1
        else:
            peak=i+1
            i+=1
    if i==len(n)-1:
        return n
    change=[0]*(len(n)-peak)
    change[0]=int(n[peak])-1
    for i in range(1,len(change)):
        change[i]=9
    last=''.join(str(change[i]) for i in range(len(change)))
    res=[]
    res.append(n[:peak])
    res.append(last)
    return int(''.join(res))
t = int(input())
for i in range(1, t + 1):
    print('Case #%d: %s' % (i, tidy()))