class AdminInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        print("Admin Information:")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
