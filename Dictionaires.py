'''
Program for a restaurant
 1 Pizza:10
 2 Burger:5
 3 Wraps:7
 4 Exit
We need to ask the customer their choices and quantity
   When Choice 4 is selected, bill must be printed and loop ended.

   d = {}
d[("Pizza, Burger, Wraps")]=(10,5,7)

print(d)
items = int(input("Which Items Do You Want?"))
'''
qty=0
bill=0
while True:
    print("1 Pizza:10\n2 Burger:5\n3 Wraps:7\n4 Exit")
    ch = int(input("Enter Your Choice: "))
    if ch>=1 and ch<=3:
        qty=int(input("Enter the Quantity: "))
    if ch ==1:
        price = qty*10
        bill = bill + price
    elif ch ==2:
        price = qty*5
        bill = bill + price
    elif ch ==3:
        price = qty*7
        bill = bill + price
    elif ch==4:
        print("Total Bill: ",bill)
        break
    else:
        print("Invalid Choice")









'''
d = {}
print(d,type(d))
d["name"]="Shilpa"
d["roll"]=11
d["marks"]=[22,23,21]
d[("age","gender")]=(36,"Female")
print(d)

print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items():
    print (k,v)
'''