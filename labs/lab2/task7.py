# - Write a Python function to sort a list of dictionaries first by the value associated with
# the key 'age', and then by the value associated with the key 'name' if the ages are equal.

def sort_dict(dict):
    sorted_dic = sorted(dict, key = lambda x:(x['age'], x['name']))
    return sorted_dic


list_of_dicts = [
{'name': 'John', 'age': 25},
{'name': 'Alice', 'age': 22},
{'name': 'Bob', 'age': 25},
{'name': 'Charlie', 'age': 22}
]
print("\n")
print("output: ", sort_dict(list_of_dicts))