n = int(input())
coffee_price = 0
total = 0
for i in range(1, n + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if (0.01 <= price_per_capsule <= 100) \
            and (1 <= days <= 31) \
            and (1 <= capsules <= 2000):
        coffee_price = (price_per_capsule * capsules) * days
        print(f'The price for the coffee is: ${coffee_price:.2f}')
        total += coffee_price
    else:
        continue

print(f'Total: ${total:.2f}')