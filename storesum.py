#using list to store the average of sum of n numbers accepted from the user
lst=[]
sum=0
avg=0
N=int(input("enter the number:"))
for i in range(0,N):
    ele = int(input())
    lst.append(ele)
    sum = sum + ele
print(lst)

avg = sum / N
print("The Sum of numbers in a list is "+str(sum))
print("The average of numbers in a list is "+str(avg))