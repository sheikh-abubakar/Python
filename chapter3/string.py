
name1 = "Abubakar"
# it will treat as  alist
name2 = name1[0:3]#it will return characters from index 0 to 2

print(name2)

print(name1[-5:-1])# -ve slicing

print(name1[3:7])# same as above

print(name1[:9])# it will start from 0 index by default

print(name1[:])# it will start from 0 index by default and end at len-1

print(name1[-5:])# it will end at len-1

#Slicing with skipping value

a = "123456789"
#first we have to extract 1:9 which is 2345678 then includng its first value
# which is '2' we have to take jump of two characters after '2' first dgit 
# always appear in result and count jump nmer from very next after first charater
# mean in this case first jump will give you '4' bcz if we start count from 3
# then two end at '4' so it will take jump tll here so and in next jump 
# it will give 6 and in next 8

print(a[1:9:2])

x = "    hello   " # use for login on production level

print(x.strip())

# ---------------------------------#

# {} -> placeholder

subject = "ICT"

std = 2

var = "In {} subject there are {} dtudents"

print(var.format(subject, std))

# for in loop

for x in subject:
    print(subject[1])


list = ["abc", "xyz"]

for y in list[1]:
    print(y)