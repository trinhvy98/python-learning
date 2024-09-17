t = (4, 1, 3, 2, 1)
print(type(t))

t1 = 1, 2, 3

print(type(t1))

t2 = (1,)
print(type(t2))

print(t.index(1))
print(t.count(1))

new_t = t + (3, 100)
print(new_t)
