l = [11,22,33,44,55,66,77]
n = len(l)

mid = n//2
leftInd = 0
rightInd = len(l)-1
for i in range(mid):
    l[leftInd],l[rightInd] = l[rightInd], l[leftInd]
    leftInd +=1
    rightInd -=1

print(l)
