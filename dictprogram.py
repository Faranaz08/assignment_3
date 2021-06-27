#Write a python program that accepts a string and builds a dictionary with
 #   LETTERS.DIGITS,UPPERCASE,LOWERCASE AS keys and
#their count as values Ex / V * T * U * e - learning123 d= {"LETTERS":12. "DIGIT":3, "UPPERCASE":3, LOWERCASE":9} .
sentence=str(input("enter a sentnce ex:VTUelearning123  "))
c=0
d=0
e=0
f=0
A=list(sentence)
print(A)
for a in A:
    if a.isalpha() == True:#checks aplabets present in a sentence
        f = f + 1
    if  a.isupper()== True:#checks upper characters present in a sentence
        c=c+1
    elif  a.islower()== True:#checks lower characters present in a sentence
        d = d + 1
    elif a.isdigit() == True:#checks digits present in a sentence
        e=e+1

dic={}
dic["letters"]=f
dic["uppercase"]=c
dic["lowercase"]=d
dic["digits"]=e
print(dic)





dictionary={

}
