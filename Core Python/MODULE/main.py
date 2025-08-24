from product import product1, product2, product3
from user import user1
from cart import Cart
from order import Order,Admin


# Create a cart for user
cart = Cart(user1)
cart.add_product(product1, 1)
cart.add_product(product3, 2)

# Place an order
order = Order(101, cart)

# Display info
print("Owner of this platform : Admin")
print("User:", user1)
print("Cart Total:", cart.total_price())
print(order)
