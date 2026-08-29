essential_spices={"cardmon","ginger","cinnamon"}
optional_spices={"cloves","ginger","black pepper"}

all_spices=essential_spices | optional_spices
print(f"All Spices: {all_spices}")

common_spices=essential_spices & optional_spices
print(f"Comon Spices: {common_spices}")


only_in_essential=essential_spices-optional_spices
print(f"only in essential:{only_in_essential}")

print(f"Is 'cloves' in essential spices?{'cloves' in essential_spices}")

