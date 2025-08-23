from typing import Final

PI: Final = 3.14159
GRAVITY: Final = 9.8

PI = 4  # ❌ Type checker will warn: Cannot assign to final name "PI"
print(PI)  # This will print 3.14159, but the assignment above is incorrect
