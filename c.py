# import heapq
# def stall():
#     total, n=map(int,input().strip().split())
#     start, end, mid = 2, total + 1, (total+3)//2
#     q = []
#     while n:
#         mid = (start + end) // 2
#         heapq.heappush(q, (-(mid-start-1), [(start, mid-1)]))
#         heapq.heappush(q, (-(end-mid-1), [(mid+1, end)]))
#         next_range = max(q[0][1])
#         if n != 1:
#             start, end = next_range
#             q[0][1].remove(next_range)
#             if not q[0][1]:
#                 heapq.heappop(q)
#         n -= 1
#     ans=[]
#     ans.append(max(mid-start, end-mid))
#     ans.append(min(mid-start, end-mid))
#     return ' '.join(str(ans[i]) for i in range(2))
#
#
# t = int(input())
# for i in range(1, t + 1):
#     print('Case #%d: %s' % (i, stall()))


def stall():
    n,k = map(int,input().strip().split())
    #level
    res=[0,0]
    level=0
    while k>0:
        k-=2**level
        level+=1
    if k == 0:
        sum_pre = 0
        for i in range(level-1):
            sum_pre += 2 ** i
        lmin=(n-sum_pre)//(2**(level-1))
        if lmin==0:
            return res
        else:
            if lmin % 2 == 0:
                res[0], res[1] = lmin // 2, lmin // 2 - 1
            else:
                res[0]=res[1]=(lmin-1)//2
    else:
        sum_pre = 0
        for i in range(level - 1):
            sum_pre += 2 ** i
        lmin = (n - sum_pre) // (2 ** (level - 1))
        carry = (n - sum_pre) % (2 ** (level - 1))
        if 2**(level-1) +k <= carry:
            space=lmin+1
        else:
            space=lmin
        if space ==0:
            return res
        else:
            if space % 2 == 0:
                res[0], res[1] = space // 2, space // 2 - 1
            else:
                res[0]=res[1]=(space-1)//2
    return ' '.join(str(res[i]) for i in range(2))

t = int(input())
for i in range(1, t + 1):
    print('Case #%d: %s' % (i, stall()))