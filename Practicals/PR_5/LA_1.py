nums = tuple(map(int, input("Enter numbers: ").split()))

print("\nTuple:", nums)

# a) total items
print("Total items:", len(nums))

# b) last item
print("Last item:", nums[-1])

# c) reverse order
print("Reverse:", nums[::-1])

# d) check 5
if 5 in nums:
    print("Yes")
else:
    print("No")

# e) remove first & last, sort
new = nums[1:-1]
sorted_new = sorted(new)
print("After removing first & last and sorting:", sorted_new)