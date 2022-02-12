#if and else

age=int(input())
if age>18:
 print('Vote is eligible')
elif age==18:
 print("Apply for voter ID")
else:
 print("You are Not eligible")

# a=5,
a=int(input())
b=int(input())
sums=0
for c in range(a,b):
 sums=sums+c
print(sums)
 
 a=float(input())
if a>10:
 print("yes")
elif a==10:
 print("equal")
else:
 print("no")
 
a=int(input())
b=int(input())
c=int(input())
if a<b and b<c:
 print("yes")
else:
 print("no")
 
a=int(input())
print(a**3)
 
for a in range(1,11):
 print(a)
 
for a in range(1,11):
 if a%2==0:
   print(a)
 
String method
#string slicing
#slice()
#indexing
 
#slice method
text="Python is a programming Language"
s1=slice(0,20,3) #start, stop, step
s2=slice(5)
s3=slice(3,6)
print(text[s1])
 
#indexing Method
text="Python is a programming Language"
 
print(text[5:16:2]) #start:Stop:step
print(text[:5])
print(text[5:])
print(text[::-1]) #reversing a string
