def try_modify_tuple(tpl, index, val):
    print("original tuple is : ",tpl)
    print("*" * 30)
    try:
        tpl[index] = val
        print("modified tuple is : ",tpl)
        print("modification successful")
    except TypeError:
        print("Modificaton failed! bcz tuples are immutable")




tpl1 = ("banana", "apple", "Mango")

try_modify_tuple(tpl1,0,"Pineapple")