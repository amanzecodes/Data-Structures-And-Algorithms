# List are:
# Heterogeneous: A single list can store multiple data types, such as integers, floats, strings, booleans, or even nested lists.
# Indexed: Elements can be accessed using both positive indices (from the start) and negative indices (from the end).
# Mutable: Lists allow modifications after creation-you can add, update, replace, or delete elements at any time.
# Ordered: Elements maintain a fixed sequence, and the order remains the same unless explicitly changed.


nums = [25, 12, 36, 95, "Me"]

names = ['random', 'string', 'exists']
mix = nums + names

nums.append("Imposter")

nums.insert(2, 77)


print(nums)



print(nums[0]) 
print(nums[4]) 
print(nums[-1])
print(nums[-5])


print("Slicing Lists: ", nums[1:4])
print("Slicing Lists: ", nums[2:])

print("Mix: ", mix)