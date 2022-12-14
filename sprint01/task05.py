def toPostFixExpression(e):
    new_e = []
    stack = []
    for i in e:
        if i.isdigit():
            new_e.append(i)
        elif i in '+-*/(':
            stack.append(i)
        elif i == ')':
            for y in stack[::-1]:
                if y == '(':
                    break
                else:
                    new_e.append(stack.pop())
    if stack:
        for _ in stack[::-1]:
            f = stack.pop()
            if f != '(':
                new_e.append(f)
    return new_e


print(toPostFixExpression(["2", "+", "3"]))
print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))
print(toPostFixExpression(["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))
