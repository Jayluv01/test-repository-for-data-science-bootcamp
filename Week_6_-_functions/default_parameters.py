
def calculate_discount(price, discount_rate = 0.10):
    """calculate pricer after discount"""
    discount_amount = price * discount_rate
    net_amount = price - discount_amount
    return net_amount

# when you call a function with a default parameter, it's okay to not provide an argument
amount1 = calculate_discount(850)
print("Amont:", amount1)

# Overriding the default parameter value for discount_rate
amount2 = calculate_discount(850, 0.25)
print("Amont:", amount2)

