class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

# Sample users
user1 = User(1, "Nitesh", "nitesh@example.com")
user2 = User(2, "Anjali", "anjali@example.com")
