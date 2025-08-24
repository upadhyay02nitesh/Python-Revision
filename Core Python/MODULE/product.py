class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} (${self.price}) - Stock: {self.stock}"

# Sample products
product1 = Product(1, "Laptop", 75000, 10)
product2 = Product(2, "Smartphone", 25000, 25)
product3 = Product(3, "Headphones", 1500, 50)
