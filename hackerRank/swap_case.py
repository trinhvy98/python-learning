def swap_case(s):
    new_lst = []

    for ch in s:
        if ch.isupper():
            char = chr(ord(ch) + 32)
            new_lst.append(char)
        elif ch.islower():
            char = chr(ord(ch) - 32)
            new_lst.append(char)
        else:
            new_lst.append(ch)

    return ''.join(new_lst)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)