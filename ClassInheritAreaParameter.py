"""The program aims to demonstrate the idea of Class Inheritance
   Create a class to input dimensions of a square
   Create two separate classes for calculating perimeter and area of square"""

class SquareSides:
    def __init__(self):
        print('Enter side of the square : ',end='')
        self.side=int(input())

class SquarePerimeter(SquareSides):
    def __init__(self):
        print('For calculating Perimeter, ',end='')
        SquareSides.__init__(self)
        self.peri=4*self.side
    def perimeter(self):
        return self.peri

class SquareArea(SquareSides):
    def __init__(self):
        print('For calculating area, ',end='')
        SquareSides.__init__(self)
        self.sq=self.side**2
    def square(self):
        return self.sq

while True:
    print('Calculate :\n1. Area\n2.Perimeter\n3.Exit\n\nEnter your choice(1/2) : ',end='')
    ch=input()
    if int(ch)==1:
        s = SquareArea()
        print(f'The area of square with side of {s.side} is {s.square()}')
    elif int(ch)==2:
        p = SquarePerimeter()
        print(f'The perimeter of square with side of {p.side} is {p.perimeter()}')
    elif int(ch)==3:
        print('Exiting from program')
        break
    else:
        print('\n\n!! Invalid choice !!')

