prices = tuple(map(int, input("Enter prices: ").split()))

print("\nPrices:", prices)

# a) total items
print("Total items sold:", len(prices))

# b) cheapest
print("Cheapest price:", min(prices))

# c) costliest
max_price = max(prices)
print("Costliest price:", max_price)

# d) ascending order
print("Ascending order:", sorted(prices))

# e) number of costliest items
count = prices.count(max_price)
print("Number of costliest items:", count)