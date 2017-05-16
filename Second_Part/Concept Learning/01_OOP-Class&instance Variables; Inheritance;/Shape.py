# an example of a class in Python

class Shape:

    description = "Simple quadrilaterals"
    author = "Bill Bulko"

    def __init__(self,length,height):
        self.x = length
        self.y = height

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2*self.x + 2*self.y

class Square(Shape):

    def __init__(self,side):
        self.x = side
        self.y = side

def main():

    myRectangle = Shape(100,45)
    print(myRectangle.author)
    print(myRectangle.description)
    print(myRectangle.x)
    print(myRectangle.y)

    myRectangle2 = Shape(50,75)
    print(myRectangle2.author)
    print(myRectangle2.description)
    print(myRectangle2.x)
    print(myRectangle2.y)

    Shape.author = "Shakespeare"

    myRectangle = Shape(100,45)
    print(myRectangle.author)
    print(myRectangle.description)
    print(myRectangle.x)
    print(myRectangle.y)

    myRectangle2 = Shape(50,75)
    print(myRectangle2.author)
    print(myRectangle2.description)
    print(myRectangle2.x)
    print(myRectangle2.y)

    print("Area of myRectangle is:",myRectangle.area())
    print("Area of myRectangle2 is:",myRectangle2.area())
    
    print("Perimeter of myRectangle is:",myRectangle.perimeter())
    print("Perimeter of myRectangle2 is:",myRectangle2.perimeter())

    mySquare = Square(30)
    print(mySquare.x, mySquare.y)
    print(mySquare.area())
    print(mySquare.author)
    
main()
