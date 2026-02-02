# Positional vs Keyword arguents

def create_customer_profile(name, age, city, purchases):
    """Create a customer profile summary"""
    print(f"Customer: {name}")
    print(f"Customer: {age}")
    print(f"Customer: {city}")
    print(f"Customer: {purchases}")

# In positional arguments, the order matters
create_customer_profile("Alice", 28, "New York", 15)

# However, in keyword arguments, order does not matter
create_customer_profile(city="Boston", name="Bob", purchases = 8, age=35)

# You can mix positional and keyword arguments. However, when you do so, positional arguments must come first.
create_customer_profile("chris", 20, city="Owerri", purchases=10 )
