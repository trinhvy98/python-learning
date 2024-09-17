"""
1. list
- []
- index
- allow duplicate
- mutable

- first index (+) - 0 | (-) - -len
- last index (+) - len - 1 | (-) - -1
2. tuple
- ()
- index
- allow duplicate
- immutable
"""
#             0.      1.        2.     3     4
#           -5       -4       -3      -2     -1
friends = ["Anna", "Kenny", "Jelly", "Bob", "Vy"]

print(type(friends))

print(friends[0])

print(friends[3])

print(len(friends))
last_index = len(friends) - 1
print(friends[last_index])

print(friends[-1])
print(friends[-len(friends)])

print('-' * 30)
print(friends)
friends.append("John")
print(friends)

friends.extend(["Ian", "Tina", "Susan"])
print(friends)

friends.insert(1,"Kristina")
print(friends)

friends = friends + ["Marry"]

print(friends)

friends += ["Lan", "Mai", "Thao"]

print(friends)

friends.remove("Marry")

print(friends)

del friends[1]

print(friends)

print(friends.pop(1))
print(friends)

# update
friends[1] = "Trang"
print(friends)

friends.reverse()

print(friends)

friends.sort()
print(friends)

print(friends.count("Vy"))

# print(friends.index("Ma"))

new_friends = friends.copy()

original = friends

print(new_friends == friends)
print(new_friends is friends)

print(original == friends)
print(original is friends)

friends.clear()

print(friends)


