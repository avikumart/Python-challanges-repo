i = 1
while i < 10:
    i = i + 1
    if i == 5:
        continue
    print(i)

# second programme to print table of 2
i = 1
number = 2
b = 9

while i <= 10:
    print(f"{number} x {i} = {number*i}")
    i = i + 1

# infinte programme demo
i =1

while i < 5:
    print("Something")
    i = i + 1 

# If-else programmes
salary = eval(input("Input the salary: "))

if salary <=0:
    print("Invalid Salary")
elif salary <= 50000:
    print("Junior manager")
elif salary <=100000:
    print("Middle-level manager")
else:
    print("Senior manager")

