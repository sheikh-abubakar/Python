def sort_tuple(tuple):
    print("before sorting: ", tuple)
    sorted_tuple = sorted(tuple, key = lambda x: x[1])
    return sorted_tuple

# sorted will apply fpr each loop on x on basis of next item an ASC
# can aslo be done by itemgetter function key = itemgetter(1)

tpl1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

print("after sorting: ", sort_tuple(tpl1))
