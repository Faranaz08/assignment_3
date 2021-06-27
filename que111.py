#write a python program to search for lines that starts with From and charcter followed by two digit number
#(00-99) and : print if greater than zero
import re
n=open(input('enter file name'))
r=n.read()
#s="adbahddhFrom00:ssss34 the way hajhdkjaa"
x=re.findall('From[0-9][0-9]:',r)
f=str(x)
d=re.findall('\d{2}',f)

print(x)
print(d)
if d>['00']:
    print(d)
else:
    print('Number is zero 0')