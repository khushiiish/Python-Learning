def chai_flavour(flavour="masala"):
   
    """Return the flavour of chai."""
    chai="ginger"
    return flavour



print(chai_flavour.__doc__)
print(chai_flavour.__name__)

def generate_bill(chai=0,samosa=0):
    """
    Calculate the total bill for chai and samosa


    :param chai:Number of chai cups (10 ruppess each)
    :param samosa:Number of samosa (15 ruppess each)
    : return:(total amount,thank you message)

    
    
    
    """
    total=chai*10 +samosa*15
    return total,"thank you for visiting"