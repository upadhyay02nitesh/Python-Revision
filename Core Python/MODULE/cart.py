from product import Product

class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_product(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def total_price(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

# Example cart
# cart1 = Cart(user1)
# cart1.add_product(product1, 1)
