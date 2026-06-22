# dictionary is used to store key value pairs .it is mutable,unordered, and don't allow duplicate
info={
"key":"value",
"name":"Khushi",
"learning":"Python",
"age":21

}
print(info)
student={
    "name":"Khushi",
    "subjects":{
        "phy":83,
        "chem":90,
        "math":99
    }
}
print(student)
print(student.values())
print(student.items())
print(student.get("name"))
print(student.update({"city":"noida"}))
# .......................SETS......................
# Collection of unordered item must be unique and immutable
collection={1,2,3,4}
print(collection)
print(type(collection))
print(len(collection))
# ..................METHOD IN SETS.........
# SET-----> ELEMENTS----->IMMUTABLE
# SETS---->ELEMENTS---->MUTABLE

collection=set()
collection.add(1)
collection.add(2)
collection.add("happy")
print(collection)
set={1,2,3}
set1={2,3,4}
print(set.union(set1))
print(set.intersection(set1))
print(set.difference(set1))

# PRACTICE
subjects={
    "python","java","c++","python","javascript","python","javascript","java"
}
print(len(subjects))