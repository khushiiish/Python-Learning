chai_order=dict(type="Masala Chau",size="large",sugar=2)
print(f"Chai order:{chai_order}")

chai_receipe={}
chai_receipe["base"]="black tea"
chai_receipe["liquid"]="milk"

print(f"Receipe base:{chai_receipe['base']}")
print(f"Receipe:{chai_receipe}")
del chai_receipe["liquid"]
print(f"Receipe:{chai_receipe}")

print(f"Is sugar in the order? {'sugar'in chai_order}")

chai_order={"type":"Ginger Chai","size":"Medium","sugar":1}

print(f"Order details (keys):{chai_order.keys()}")
print(f"Order details (values):{chai_order.values()}")
print(f"Order details (items):{chai_order.items()}")




extra_spices={"cardamon":"crushed","ginger":"sliched"}
chai_receipe.update(extra_spices)

print(f"updated chai receipe:{chai_receipe}")

chai_size=chai_order["size"]
print(f"Chai size is:{chai_size}")