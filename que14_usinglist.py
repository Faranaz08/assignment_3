#write a program to accept a USN and marks obtained from the user find the max and min
#and student usn who scored in the range 100-85 84-75 74-60 below 60 seprately
lst=list()
lst1=list()
lst2=list()
lst3=list()
lst4=list()
N=int(input("Enter the number of students"))
for i in range(0,N):
    USN=input("USN:")
    marks1=input("mark1:")
    lst.append((marks1,USN))
print("maximum :",(max(lst)))
print("minimum: ",(min(lst)))
for key, value in lst:
    if key>'85' and key<='100':
        lst1.append(value)
    elif key>'75' and key<='85':
        lst2.append(value)
    elif key>'65' and key<='75':
        lst3.append(value)
    elif key<='60':
        lst4.append(value)
print("in btw 85- 100")
print(lst1)
print("in btw 75- 85")
print(lst2)
print("in btw 65- 75")
print(lst3)
print("below 60")
print(lst4)