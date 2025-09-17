# A Python dictionary is a built-in data structure that stores data in key-value pairs.

my_dic = {
    "name" : "Ali",
    "age" : 22,
    "age" : 21
}

# print(my_dic.get("name"))


# print(my_dic["age"])

# loop

# for dic in my_dic:
#     print(dic, my_dic[dic])

# key value syntax for dictionaries for loop

for key, val in my_dic.items():
    print(key, val)

my_dic["gender"] = "male"

y = my_dic.keys()
x = my_dic.values()

print(x, y)



if "age" in my_dic:
    print("yes")