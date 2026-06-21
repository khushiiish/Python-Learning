print("Hello worlld")
#variables
name="khushi"
age=21
course="btech"
print(name)
print(age)
print(course)
print(type(name))
print(type(age))
print(type(course))
# data types:1.Integers 2.String 3.Float 4. Boolean  5.None

# single line comment
# """multi-line comment"""

#Operator
#Airthmetic Operator
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #remainder
print(a **b) #power
#Relational operator
a=50
b=20
print(a==b)#False
print(a!=b)#true
print(a>=b)#true
print(a<=b)#false
print(a>b)#true

#assignment operator
num=10
num1=num+10 
num *=5
print(num)
#Logical operator
print(not False)
print(not True)
val1= True
val2= False
print("and operator:",val1 and val2)
print("or operator:",val1 or val2)
#type conversion
a=2
b=4.25
sum=a+b #2.0+4.25=6.25
print(sum)

#input in python
name=input("enter your name:")
print("welcome",name)
name=input("enter name:")
age=input("enter age:")
marks=input("enter marks:")
print("welcome",name)
print("age=",age)
print("marks=",marks)


#######################################
#PRACTICE 
#WAP TO INPUT 2 NUMBERS AND PRINT THEIR SUM
first=int(input("enter first:"))
second=int(input("enter second:"))
sum=first+second
print("sum=",sum)
#