# l=[11,2,33,4,5,1] =>          a=[33,11,5]          b = [4,2,1]

l=[11,2,33,4,5,1]

def A():
    l.sort(reverse=True)
    return (l[0:3])

# -4 -2 -6
def B():
    l.sort(reverse=True)
    return (l[3::])

print("",A(),"\n",B())


