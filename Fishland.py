price_kg_skumr = float(input())
price_kg_caca = float(input())
price_kg_palamud = price_kg_skumr + (price_kg_skumr * 0.6)
price_kgsafrid = price_kg_caca + (price_kg_caca * 0.8)
kg_palamud = float(input())
kg_safrid = float(input())
kg_shells = int(input())

price_shells = kg_shells * 7.5
price_palamud = kg_palamud * price_kg_palamud
price_safrid = kg_safrid * price_kgsafrid

print(f"{price_safrid + price_palamud + price_shells:.2f}")
