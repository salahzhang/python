# def flip():
#     s, k = input().strip().split()
#     k = int(k)
#     b = s.strip().split('+')
#     for i in range(len(b)):
#         if b[i] != '':
#             b[i] = -len(b[i])
#         else:
#             b[i] = 1
#     i=1
#     while i<len(b):
#         if b[i - 1] > 0 and b[i] > 0:
#             b[i - 1] += b[i]
#             b.remove(b[i])
#         else:
#             i+=1
#     for i in range(len(b)):
#         if b[i]>0:
#             b[i]+=1
#     cnt = 0
#     if b[0]<0 and b[0]%k== 0:
#         cnt += (-b[0]//k)
#         b[0] *=-1
#     if b[-1]<0 and b[-1]%k== 0:
#         cnt += (-b[-1]//k)
#         b[-1]*=-1
#     for i in range(1, len(b) - 1):
#         if b[i] > 0 and b[i - 1] == b[i + 1] and b[i] - b[i - 1] == k:
#             cnt += 2
#             b[i - 1] = b[i + 1] = -b[i - 1]
#     for i in range(1,len(b)):
#         if b[i - 1] == b[i] and b[i - 1] == 1 - k:
#             cnt += 2
#             b[i - 1] = b[i] = -b[i]
#     if min(b) < 0:
#         return "IMPOSSIBLE"
#     else:
#         return cnt
def flip():
    s,k= input().strip().split()
    k = int(k)
    ans=[]
    for i in range(len(s)):
        ans.append(s[i])
    cnt=0
    for i in range(len(ans)):
        if ans[i]=='+':
            continue
        else:
            if len(ans)-i>=k:
                for j in range(i,i+k):
                    if ans[j]=='-':
                        ans[j]='+'
                    else:
                        ans[j]='-'
                cnt+=1
            else:
                return "IMPOSSIBLE"
    return cnt

t = int(input())
for i in range(1, t + 1):
    print('Case #%d: %s' % (i, flip()))