def validParentheses(s):
    matching_brackets = {'[': ']', '{': '}', '(': ')'}
    stack = []
    for char in s:
        if char in matching_brackets:
            stack.append(matching_brackets[char])
        elif not stack or stack.pop() != char:
            return False
    return len(stack) == 0



print(validParentheses('([]{}())'))
