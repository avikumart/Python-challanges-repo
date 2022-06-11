# programming in python 
# first programme 
mytuple = (10,20,70,65,8,11,3,90)
maxi=mytuple[0]

for k in range(len(mytuple)):
    if mytuple[k]>maxi:
        maxi=mytuple[k]
	        
print("maximum element is: ", maxi)

# second programme 
# digits and numbers calculator
mystring = input("Enter the alphanumeric string: ")
mydicts2 = {"numbers":0, "letters":0}

for x in mystring:
    if x.isdigit():
        mydicts2['numbers'] +=1
    elif x.isalpha():
        mydicts2['letters'] +=1
    else:
        pass 

print("My digits are: ", mydicts2['numbers'])
print("My letters are: ", mydicts2['letters'])