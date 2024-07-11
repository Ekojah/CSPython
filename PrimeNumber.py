nums = int(input("List Your Numbers: "))
#







'''
#to preform the equation with any given number length in variable n(input
def getcount(n):
    count=0
    while n>0:
        count=count+1
        n = n//10
    return count
#When Seperated
n = int(input("Enter the number: "))
#The Squared Value of All Numbers
sum = 0
origin=n
power = getcount(n)
while n>0:
    r = n%10
    sum = sum+ r**power
    n = n//10
#Sum to the original number.
if origin==sum:
    print("Armstrong Num")
else:
    print("Not an armstrong num")
    
    
n = input("Enter the n value: ")
#if the inputted value is = to the inputted value when reversed
if n==n[::-1]:
    print("Palindrome")
else:
    print("not palindrome")

n = int(input("Enter the n value: "))
orig = n
rev = 0
while n>0:
    r = n%10
    rev = rev*10+r
    n = n//10
print("Rev: ",rev)

prime_num = int(input("Enter Your Prime Number "))

outlier = 2
while outlier<prime_num:
    if prime_num%outlier==0:
        print("this is a prime number")
        break
else:
    print("this is not a prime number: ",prime_num)

    n = int(input("List out your numbers: "))

sum = 0
for x in range n:
    sum =sum+int(x)
else:
    print("sum of digits = ",sum)
'''



