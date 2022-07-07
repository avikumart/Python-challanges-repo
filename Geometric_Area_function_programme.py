# area of geometric object finder programme
choice = int(input(print("choose from 1 for square, 2 for ractangle, 3 for circle, 4 for triangle: ")))

if choice==1:
    def area_square():
        side = eval(input("Enter side of the square: "))
        print("Area of square is: ", side*side)
    area_square()
elif choice ==2:
    def area_rectangle():
        l, b = eval(input("Enter the length and breadth of ractangle: "))
        print("Area of ractangle is: ", l*b)
    area_rectangle()
elif choice == 3:
    def area_circle():
        rad = eval(input("Enter the radious of circle: "))
        print("area of circle is: ", 3.14*rad*rad)
    area_circle()
elif choice ==4:
    def area_triangle():
        base, p = eval(input("Enter length of base and height: "))
        print("Areaof triangle is: ", 0.5*base*p)
    area_triangle()
else:
    print("Incorrect choice!")
