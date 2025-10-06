def merge_lists(l1, l2):
    result = []
    for i in range(max(len(l1), len(l2))):
        if i < len(l1) and i < len(l2):
            if isinstance(l1[i], int) and isinstance(l2[i], int):
                result.append(l1[i] + l2[i])
            else:
                result.append(l1[i] + l2[i])
        elif i < len(l1):
                result.append(l1[i])
        else:
                result.append(l2[i])
    return result

list1 = [1, 'hello', 3]
list2 = [2, 'world', 4, 5]

print("output: ", merge_lists(list1, list2))
