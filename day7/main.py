"""
dict
{k1: v1, k2: v2, k3: v3, ...}
"""
# d = {1: 'a', 2: 'b'}
#
# print(type(d))
#
# print(d[1])
#
# print(d[2])
#
# d[3] = 'c'
#
# print(d)

# student_marks = {
#     'anna': [40.0, 70.0, 80.0],
#     'vy': [70.0, 80.0, 90.0],
#     'kenny': [30.0, 45.0, 60.5]
# }
#
# print('kenny' in student_marks)
#
# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# scores = [x[-1] for x in students]
#
# min_score = min(scores)
# second_lowest_grade = min([x for x in scores if x != min_score])
#
# students.sort(key=lambda x: (-x[-1], -ord(x[0][0])))
# print(students)
#
# for name, score in students:
#     if score == second_lowest_grade:
#         print(name)

# split
# convert string to list of strings
s = "a---b-c"
s = "a                                        b                      c"
# s = ' '
# ['a', 'b', 'c']

lst = s.split()

ans = '$'.join(lst)
print(ans)

# join - convert list of strings to a string
lst = ['a', 1, 2, 3, 4]

# new_lst = [str(x) for x in lst]
# new_lst = []
#
# for x in lst:
#     new_lst.append(
#         str(x)
#     )
new_lst = map(str, lst)
# 1-2-3-4
ans = '-'.join(new_lst)
print(ans)

