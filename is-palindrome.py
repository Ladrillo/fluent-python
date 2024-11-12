def isPalindrome(x):
    stringified = str(x)
    reversed = stringified[::-1]
    return stringified == reversed

print(isPalindrome('1234'))
print(isPalindrome('121'))
