#python program to search the line starts with X followed by a nonwhitespace charcter
#followed by ':' ending with number .Display the sum off all the numbers
import re
s=open('abc.txt','r')
total=0
lst = []
lst1 = []
for a in s:
    pat = re.findall(r'^X\S:\d*', a)
    s1 = str(pat)
    nums = re.findall('\d+', s1)
    lst.append(nums)
    print(pat)
for i in range(0, len(lst)):
    lst1 = lst1 + lst[i]
    for i in range(0, len(lst1)):
        lst1[i] = int(lst1[i])


print(str(lst1))

total=sum(lst1)

print(total)