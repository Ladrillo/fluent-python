def needle_haystack(haystack, needle):
    needle_length = len(needle)
    for index, _ in enumerate(haystack):
        the_slice = haystack[index:(index + needle_length)]
        if the_slice == needle:
            print(index, the_slice)
            return index
    print("not foundsees")
    return -1


needle_haystack("mississippi", "a")
