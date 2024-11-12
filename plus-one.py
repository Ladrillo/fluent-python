def plusOne(digits):
    digits_as_strs = map(str, digits)
    joined_digits = "".join(digits_as_strs)
    parsed_num = int(joined_digits)
    incremented_num = parsed_num + 1
    stringified_num = str(incremented_num)
    result = [int(digit) for digit in stringified_num]
    return result


print(plusOne([1, 2, 3]))
