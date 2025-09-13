def avg():
    a = int(input ("enter num1: "))
    b = int(input ("enter num2: "))
    print("avg is : ", int((a+b)/2))

avg()

# Keyword Arguments

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
