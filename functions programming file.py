# functions programming file
def demo(name, age=29):
    print(name, age)
demo("arpita", 25)

# second programme to find sum of list of numbers
def sum_function(value):
    iteable = list(value)
    sum = 0 
    for i in iteable:
        sum = sum + i
    return sum
    print(sum)

sum_function([2,5,8,4])