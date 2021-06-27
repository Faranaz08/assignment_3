#write a py program accept N numbers from the user and find the sum of even numbers
#product of odd numbers in enterd in a list
lst=[]
even=[]
odd=[]
sum=0
prod=1
N=int(input("enter the N number:"))
for i in range(0,N):
    ele = int(input())
    lst.append(ele)
    if ele%2==0:
        even.append(ele)

        sum=sum+ele
    else:
        odd.append(ele)

        prod=prod*ele

print(lst)
print("Even numbers :" +str(even))
print("odd numbers :" +str(odd))
print("the sum of even numbers in list :"+str(sum))
print("the product of odd numbers in the list :"+str(prod))
