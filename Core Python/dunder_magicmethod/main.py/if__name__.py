# 💡 Summary in one line:

# if __name__ == "__main__": ensures some code runs only when the
# file is executed directly,
# not when imported.


# if __name__ == "__main__": is useful because it prevents code from running on import,
# allows reusability, 
# and lets you test or run scripts safely without affecting other programs.


def calculate_total_price(a,b):
    return a + b


if __name__ == "__main__":
   a=10
   b=20
   print("Total Price:", calculate_total_price(a, b))