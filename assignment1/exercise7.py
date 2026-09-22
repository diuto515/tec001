import random
code_3_digit = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
code_4_digit = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"
print(f"3-digit code: {code_3_digit}")
print(f"4-digit code: {code_4_digit}")
