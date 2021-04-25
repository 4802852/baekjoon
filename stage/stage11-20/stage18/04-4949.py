import sys

while 1:
    n = str(sys.stdin.readline())
    if n == '.\n':
        break
    isbalanced = True
    stack = []
    for i in range(len(n)):
        if not isbalanced:
            break
        if n[i] == '(' or n[i] == '[':
            stack.append(n[i])
        if n[i] == ')':
            if stack and stack.pop() == '(':
                pass
            else:
                isbalanced = False
                break
        elif n[i] == ']':
            if stack and stack.pop() == '[':
                pass
            else:
                isbalanced = False
                break
    if stack or not isbalanced:
        print('no')
    else:
        print('yes')