#Question 1
l1=[1,2,3,4,5]
print(list(reversed(l1)))

#Question 2
u=input("Enter A string")
for i in range(len(s)):
    if u[i].isupper():
        print(u[i])

#Question 3
s=input("Enter Values").split(",")
l=[]
for i in s:
    l.append(int(i))
print(l)

#Question 4
x=int(input("Enter no."))
y=x
f=0
re=0
while x!=0:
    f=x%10
    re=re*10+f
    x//=10
if y==re:
    print("Palandromic")
else:
    print("Not a Palandromic")



#Question 5
from copy import *
print("DeepCopy:- ")
list1 = ['a','b',['ab','ba']]

list2 = deepcopy(list1)

list2[2][1] = "d"
list2[0] = "c";

print(list2)
print(list1)
print("Shallow Copy:- ")
list3=list1
list3[0]="hi"
print(list3)
print(list1)
"""A shallow copy constructs a new compound object and then inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."""
