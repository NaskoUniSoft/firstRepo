w = float(input())
h = float(input())

w *= 100
h *= 100
h -= 100

w = int(w)
h = int(h)

h = h // 70
w = w // 120
seat = h * w -3

print(seat)