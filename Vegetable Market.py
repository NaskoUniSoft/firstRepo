# 1 euro = 1.94 lv.

price_per_kg_vegetables = float(input())
price_per_kg_fruit = float(input())
total_kg_veg = int(input())
total_kg_fruit = int(input())
total_price = price_per_kg_fruit * total_kg_fruit + price_per_kg_vegetables * total_kg_veg
print(f"{total_price / 1.94:.2f}")