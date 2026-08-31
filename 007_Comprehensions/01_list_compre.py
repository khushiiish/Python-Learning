#Comprehensions are a concise way to create list,sets,dictionaries or generators in python using a single line of code
#filter item , transform item ,create a new collection ,flatten nested structure
#what purpose do they serve?
#cleaner code,faster execution
5#types of comprehension 
#List    , Set, Dictionary,GenerATOR


#SYNTAX:-     [EXPRESSION FOR ITEM IN ITERABLR IF CONDITION]


menu=[
    "Msala Chau",
    "Iced Lemon Tea",
    "Green tEA",
    "Iced pEACH TEA",
    "Ginger Tea"
]
iced_tea=[tea for tea in menu if "Iced" in tea]

print(iced_tea)