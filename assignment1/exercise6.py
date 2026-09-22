talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_lots = (talents * 20 * 32) + (pounds * 32) + lots
total_grams = total_lots * 13.3
kg = int(total_grams / 1000)
grams = total_grams % 1000
print("\nThe weight in modern units:")
print(f"{kg} kilograms and {grams:.2f} grams.")
