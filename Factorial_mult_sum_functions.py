# factorial function
def factorial(num):
    if num == 0:
        return 1
    else:
        multiplication = num*factorial(num-1)
    return multiplication

factorial(5)
factorial(10)

# multiplication of all the combinations
def multiply(l1, l2):
    results = []
    for i in l1:
        for j in l2:
            mul = i*j
            results.append(mul)
    return results

multiply([1,2], [3,4])

# multiplication of number in list
def mult_list(lst):
    results = 1
    for i in lst:
        results = results*i
    return results

mult_list([1,2,3,5,10])

# sum of the elements in list
def sum_list(l):
    result = 0
    for i in l:
        result = result + i
    return result

sum_list([1,2,5,7,10])

# return statement function
def  multi():
    a =3
    b =6
    c =a*b
    return c

c = multi()
print(c)