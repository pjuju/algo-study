def make_exp(text):
    stack = []
    exp = ''
    isp = {'(': 0, '+': 1, '-':1, '*': 2, '/':2}
    icp = {'(': 3, '+': 1, '-':1, '*': 2, '/':2}
    for a in text:
        if a not in '(+-/*':
            exp += a
        else:
            if a == ')':
                while stack[-1] != '(':
                    exp += stack[-1]
                    stack.pop()
                stack.pop()
            elif not stack:
                stack.append(a)
            else:
                if icp[a] > isp[stack[-1]]:
                    stack.append(a)
                else:
                    while stack and not icp[a] > isp[stack[-1]]:
                        exp += stack[-1]
                        stack.pop()
                    stack.append(a)
    while stack:
        exp += stack[-1]
        stack.pop()

    return exp

ans = make_exp(input()).replace('(','').replace(')','')
print(ans)
