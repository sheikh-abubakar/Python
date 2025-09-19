# e.g1

numbers = [1, 2, -3, 4, -5, 6]

count = 0

for num in numbers:
    if num < 0:
     count +=1

# print("total -ve numbers: ", count)

# table example

number = 2

for i in range(1, 12):
    # skip 11
    if i == 11:
        continue

    # print(number,'x', i, '=', number*i)

#reverse a string 
# range The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

str = "hello"
rev_str = ""
for s in range(len(str)-1, -1, -1):
   rev_str += str[s]
print(rev_str)


# first non-repeated char
# .count method
str = "bannana"

for s in str:
    if str.count(s) == 1:
       print(s,'comes one times')
       break


