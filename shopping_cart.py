customer = input("Customer Name: ")
print()

products = []

price = 0
for i in range(3):
    product_name = input(f"Product {i+1}: ")
    product_price = int(input("Price: "))

    products.append((product_name, product_price))
    price = price + product_price
    print()

total_price = int(price)
print(f"Customer Name: {customer}")
print()

for i, (product_name, product_price) in enumerate(products):
    print(f"Product {i+1}: {product_name}")
    print(f"Price: {product_price}")
    print()

print(f"Subtotal: {total_price}")

if price >= 5000:
  discount = 0.2
elif price >= 3000 and price < 5000:
  discount = 0.1
elif price >= 1000 and price < 3000:
  discount = 0.05
elif price < 1000:
  discount = 0
else:
  discount = "Invalid"

discount_price = total_price * discount
final_price = total_price - discount_price

print(f"Discount: {int(discount_price)}")
print(f"Final Total: {int(final_price)}")
