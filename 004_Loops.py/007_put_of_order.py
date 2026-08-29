flavours=["Ginger","Out of Stock","Lemon","Discountinued","Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        
        print("Discontinued item found") 
        break
print(f"Out of Loop") 


staff=[("Amit",16),("Zara",17),("Raj",15)]

for name,age in staff:
    if age<=18:
        print(f"{name} is eligible to manage the staff")
        break
else:
        print(f"No one is eleigible")