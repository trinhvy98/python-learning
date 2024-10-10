a = set()
a.update([1, 2, 3])

b = {3, 4, 5}

print(a.union(b))
print(a.symmetric_difference(b))
print(a.intersection(b))

c = range(1, 10)
user_number = int(input("enter a number: "))

if user_number in c:
    print("ur number is in the range")
elif user_number < c[0]:
    print("too low")
else:
    print("too high")
