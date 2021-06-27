#program to read all the lines in a file accepted from the user and print all email ids contained in it.

import re
fhand = open('mbox.txt')
f=fhand.read()
#f="faranazannigeri@gmail.com a bc cd  faranazanni3142@gmail.com"
#d=f.split()
#print(d)
#print(f)
#for line in f:
    #line = line.rstrip()
x = re.findall('\S+@\S+',f)
for d in x:
    print(d)



#print(x)

#print(line)


