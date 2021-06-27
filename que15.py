#wpp to search for the line stars with F followed by two charcters then followed by m
import re
n=open(input('enter file name'))

#s="F$&m"
for i in n:
    i = n.readline()

    x = re.findall('F..m', i)

    if x:
        print(x)
#mbox.txt