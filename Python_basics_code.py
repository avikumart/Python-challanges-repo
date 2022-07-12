lst = [1,1,2,2,2]
lst.count(2)
lst.insert(2,1)
print(lst)
lst.pop(1)
print(lst)

dct = {"g":1,
        "b":2}
dct.clear()
print(dct)

p1=('google', 'Microsoft', 'IBM', 'Amazon')

p2= p1+p1

print(len(p2))

def func1(number):
    return number*number
print((func1(5)))

a=1
while(a==1):
    print("welcome")
    a=int(input("Enter your choice -->0/1:"))
    
bag= ['tea','sugar','bread','butter']

for i in range(len(bag)):

    if bag[i] == 'sugar':
        print('jaggery')
    else:
        print(bag[i])
        

for i in range(8):
    for j in range(5):
        if j == 3:
            break
    print(j)
print(i)

d=-20 

while(d>0):

    print(d)

if(d<0):

    print(-1*d)
    
if 1 + 3 == 7:
    print("Rahul is right")
else:
    print("Rahul is wrong")
    
for i in [1,2,3,4]:
    print("*")
    
for letter in 'Python':
    if letter == 'o':
        continue
    print('Current Letter : ' + letter)
    

number = 8
while number <= 8:
    if number < 8:
        number = number + 1
    print(number)
    
print([i for i in range(11)])

while(not 1):
    print(1)
    
b = [1, 2, 3]
print(b * 3)

def func(x):
    return x*5
func(3)