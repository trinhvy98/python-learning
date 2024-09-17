lst = [[1, 2, 3], [4, 5], [(True, 2.3)]]
print(type(lst))
print(len(lst))

print(lst[0])

print(lst[0][2])
print(lst[1][1])

lst[1].append(6)
print(lst)

lst.append("Vy")
print(lst)
print(lst[2][0][-1])