def is_balanced(s):
    count = 0
    for symbol in s:
        if symbol == '(':
            count += 1
        elif symbol == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


print(is_balanced('()'))
print(is_balanced('())'))
print(is_balanced('(()'))
print(is_balanced(')())'))
print(is_balanced('))(('))