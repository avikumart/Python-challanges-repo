# lambda functions
numbers_list = [x for x in range(20)]
print(numbers_list)

# filtered list
filter_lst = list(filter(lambda x : x%2 == 0, numbers_list))
print(filter_lst)

# map function
mapping = list(map(lambda x : pow(x,3), filter_lst))
print(mapping)

# functions challange
def function1(number):
    num = number + 25
    return num

# 2
def function(name, age=20):
    print(name, age)
    
num = function1(5)
function('Ananda', num) 