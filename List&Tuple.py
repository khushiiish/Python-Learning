marks=[94.4,87.5,66.4,45.1]

print(marks)
print(type(marks ))
print(marks[0])
print(marks[1])
print(marks[1:4])
print(marks[1:])
print(marks[-3:-1])
"""we can store differnt types of datatype in one list.list are mutable while strings are immutable"""
student=["khushi",99,17,"delhi"]
print(student[0])
student[0]="anuj"
print(student)
"""............List Methods........."""
list=[2,1,3,4,5]
list.append(6)#adds one element at te end
print("After appending",list)
print(list.sort())# sort in ascending order
print("After sorting",list)
print(list.sort(reverse=True))# sort in descending order
print("after reverse",list)
print(list.reverse())
print("reversed",list)
print(list.insert(5,8))#insert at the specific index
print("inserted value",list)

"""..............Tuples..(immutable).........."""
tup=(2,1,3,4,5)
print(tup[0])
print(tup[1])

print(tup)
"""........Tuple Methods........"""
tup=(11,22,33,44,55)
print(tup.index(44))#returns index of first occurence
print(tup.count(33))#counts total occurences
#PRACTICE
#WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVUORITE MOVIE AND STORE THEM IN A LIST
movies=[]
movies.append(input("enter 1st movie"))
movies.append(input("enter 2nd movie"))
movies.append(input("enter 3rd movie"))

print(movies)

#palindrome or not
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")
