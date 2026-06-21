"""if-elif-else (Syntax)"""
light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
else:
     print("wait")
marks=int(input("enter student marks:"))
if(marks>=90):
    grade="A"
         
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D" 
print("grade of the student",grade)     
"""..............nesting.............."""
age=34
if(age>=18):
    if(age>=80):
      print("cannot drive")
    else:
       print("can drive")
else:
    print("cannot drive")          


