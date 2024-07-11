#    0  1  2  3  4  5  6
t = (11,22,33,44,55,66,77)
#    -7 -6 -5 -4 -3 -2 -1

print(t[:])
print(t[2:5])
print(t[-1:-3])
print(t[2::3])
print(t[::2])
print(t[0:3:6])
print(t[-2:-1])
print(t[5:-6:-1])
print(t)
'''
t = (77,)
print(t, type(t))
t1 = (11,22,33,44)
t2 = (1,2,3)
#concatenation operator
t3 = t1+t2
#replication operator
t4 = t1*3
print(t3)
print(t4)
#membership operators
print(777 in t1)
print(777 not in t1)
for x in t1:
    print(x)
    '''