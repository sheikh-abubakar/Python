
def rotate_tpl(tpl, position):
    #slicing
    val = position % len(tpl)
    #[-2:] + [:-2]
    return tpl[-val:] + tpl[:-val]

tuple = (1, 2, 3, 4, 5)

print("output: ", rotate_tpl(tuple, 2))