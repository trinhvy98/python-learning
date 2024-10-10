"""
lst = [3, 1, 2]
# [4]

# ans = []
#
# for x in lst:
#     if x % 2 == 0:
#         ans.append(x*2)

ans = [x*2 for x in lst if x % 2 == 0]  # list comprehensions
print(ans)
"""
# numbers = [int(x) for x in input().split()]
# numbers = list(map(int, input().split()))
#
# print(numbers)

first = "Ross"
last = "Taylor"
# Hello Ross Taylor! You just delved into python.

print(f"Hello {first} {last}! You just delved into python.")
