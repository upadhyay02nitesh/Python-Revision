# -----------------------------
# 1️⃣ Authentication Decorator
# -----------------------------
def auth_decorator(func):
    def wrapper(*args, **kwargs):
        print("🔑 Checking Authentication ....... ")
        valid_users = ["Kalu", "Nitesh", "Admin"]
        
        if args and args[0] in valid_users:
            print("✅ Authentication Successful")
            return func(*args, **kwargs)
        else:
            print("❌ Authentication Failed")
            return None
    return wrapper

# -----------------------------
# 2️⃣ Admin Role Decorator
# -----------------------------
def admin_only(func):
    def wrapper(*args, **kwargs):
        print("🔒 Checking Admin Access ....... ")
        admin_users = ["Admin"]
        if args and args[0] in admin_users:
            print("✅ Admin Access Granted")
            return func(*args, **kwargs)
        else:
            print("❌ Admin Access Denied")
            return None
    return wrapper

# -----------------------------
# 3️⃣ Login Function
# -----------------------------
@auth_decorator      # first check authentication
@admin_only          # then check admin
def login(user):
    print(f"🎉 Welcome, {user}!")

# -----------------------------
# Test Cases
# -----------------------------
print("\n--- Test 1: Admin ---")
login("Admin")   # ✅ Authentication + Admin

print("\n--- Test 2: Normal User ---")
login("Kalu")    # ✅ Authentication, ❌ Admin

print("\n--- Test 3: Hacker ---")
login("Hacker")  # ❌ Authentication
