l = [11,22,33,44,55,66,77]
temp = l[0]
n = len(l)
for i in range(n-1):
    l[i] = l[i+1]
else:
    l[n-1] = temp

print(l)


'''
def lin_search ():
flag=0
    for search in len(l):
        if l[i] == key:
            print("Key Found At: ",i)
        else:
            print("Search Key Not Found")
            break

l= [1,3,4,5,6,7,8,9,9,]
key = int(input("Enter the search Key: "))
lin_search()

'''
