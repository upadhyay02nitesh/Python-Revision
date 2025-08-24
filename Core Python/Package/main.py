from Admin.admininfo import AdminInfo
from Seller.sellerinfo import SelllerInfo
from User.userinfo import UserInfo

a=AdminInfo("Alice", "alice@example.com", "123-456-7890")
print()
b=SelllerInfo("Bob", "bob@example.com", "098-765-4321")
print()
c=UserInfo("Charlie", "charlie@example.com", "555-555-5555")

a.display_info()
b.display_info()
c.display_info()