def is_balanced(s):
    count = 0
    for symbol in s:
        if symbol == '(':
            count += 1
        elif symbol == ')':
            if count == 0:
                return False
            count -= 1
    return count == 0


print(is_balanced('()'))
print(is_balanced('())'))
print(is_balanced('(())'))
print(is_balanced(')())'))
print(is_balanced('))(('))
