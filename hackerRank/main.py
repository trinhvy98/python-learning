s = "thao                          vy"
# Thao  Vy

words = s.split(' ')

print(words)

new_lst = []

# for word in words:
#     if len(word) != 0:
#         first_letter = word[0].upper()
#         rest_chars = word[1:].lower()
#         new_string = first_letter + rest_chars
#         new_lst.append(new_string)
#     else:
#         new_lst.append(word)

for word in words:
    if len(word) != 0:
        new_lst.append(word.())
    else:
        new_lst.append(word)

print(' '.join(new_lst))
