from cart import Cart

Admin="Nitesh Upadhyay"
class Order:
    def __init__(self, order_id, cart):
        self.order_id = order_id
        self.cart = cart
        self.status = "Pending"

    def __str__(self):
        return f"Order {self.order_id} for {self.cart.user.name}, Total: ${self.cart.total_price()} - Status: {self.status}"
