a = set()
# a = {}

print(len(a))
print(type(a))
print(a)

a.add(100)
a.add(100)
a.update([1, 2, 3])
a.update((4, 5, 6))
a.update({"b": 7, "c": 8, "d": 9})
a.update({10, 11, 12})
a.remove(100)
# a.remove(200000)
# b = {([1], 2, 3)}

# print(a.pop())
a.discard(200000)

b = a.copy()
print(a == b)
