# Program for learning Mutability and Equality

def updateVars(a,b):
    a = 5
    b[2] = "new two"

def main():

    x = 10
    y = [ "zero", "one", "two", "three" ]

    print ("x = ", x)
    print ("y = ", y)

    updateVars(x,y)

    print ("x = ", x)
    print ("y = ", y)


main()
