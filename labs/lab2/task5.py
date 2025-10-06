def tpls_to_dict(tuple):
    result = {}
    for key, val in tuple:
        result[key] = val
    return result

list_of_tuples = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]

print("output: ", tpls_to_dict(list_of_tuples))