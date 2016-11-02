import turtle
import math

def square(p):
    """
    Draws a square
    :param p: denotes the length of each side of square
    :return: None
    :pre: (relative) pos (0,0) heading (east), pen down
    :post: (relative) pos (0, -p) heading (south), pen down
    """
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(3*p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    turtle.forward(p)
    turtle.left(90)
    return None


def antenna(t,depth,size):
    """
    Function when called recursively draws the fractal antenna as a sequence of squares
    :param t: turtle object
    :param depth: level of fractal
    :param size: size of antenna
    :return: None
    :pre: (relative) pos (0,0) heading (East), pen up
    :post: (relative) pos (0,0) heading (East), pen up
    """

    if (depth == 1):
        t.pendown()
        for _ in range(4):
            square(size)
        t.penup()

    else:
        for i in range(5):
            antenna(t,depth - 1, size)
            if i == 0:
                t.left(45)
                if depth > 2:
                    t.penup()
                    t.left(90)
                    t.forward((3+ 9 * (depth - 3)**2) * (math.sqrt(2)) * size)
                    #t.forward((3 + counter) * (math.sqrt(2)) * size)
                    #counter += 3 ** (depth - 1)
                    t.right(90)
                    #t.home()
                t.forward((3**(depth-1))*(math.sqrt(2))*size)      #going to its east
                t.right(45)
            elif i == 1:
                t.left(45)
                if depth > 2:
                    t.penup()
                    t.left(90)
                    #t.forward((3+ 9 * (depth - 3)) * (math.sqrt(2)) * size)
                    t.forward((3 + 9 * (depth - 3) ** 2) * (math.sqrt(2)) * size)
                    t.right(90)

                t.penup()
                t.forward(-(2*(3**(depth-1)))*(math.sqrt(2)) * size)  # going to its west
                t.right(45)
            elif i == 2:
                t.left(45)
                t.penup()
                if depth > 2:
                    t.penup()
                    #t.home()
                    t.left(90)
                    #t.forward((3 + 9 * (depth - 3)) * (math.sqrt(2)) * size)
                    t.forward((3 + 9 * (depth - 3) ** 2) * (math.sqrt(2)) * size)
                    t.right(90)
                    t.forward((3 ** (depth - 1)) * (math.sqrt(2)) * size)
                    t.left(90)
                    t.forward((3 ** (depth - 1)) * (math.sqrt(2)) * size)
                else:
                    t.forward((3 ** (depth - 1)) * (math.sqrt(2)) * size)
                    t.left(90)
                    t.forward((3**(depth-1))*(math.sqrt(2))*size)       # going to its north
                t.right(135)
            elif i == 3:
                t.right(45)
                if depth > 2:
                    t.penup()
                    t.forward((6 + 9 * ((depth - 2)**2)) * (math.sqrt(2)) * size)
                    #t.forward((((3 ** (depth - 1)))) * (math.sqrt(2)) * size)
                    t.left(45)
                else:
                    t.penup()
                    t.forward(((2*(3**(depth-1))))*(math.sqrt(2)) * size)   # going to its south
                    t.left(45)


            else:

                return None


def edgeWithSpace(t, depth, size):
    """
    Function when called recursively draws the fractal antenna as a single line with space (not touching)
    :param t: turtle object
    :param depth: level of fractal
    :param size: size of antenna
    :return: None
    :pre: (relative) pos (0,0) heading (East), pen down
    :post: (relative) pos (size, 0) heading (East), pen down
    """
    if depth == 0:
        t.forward(size)

        return
    else:
            edgeWithSpace(t, depth - 1, size / 3)
            t.left(90)
            edgeWithSpace(t, depth - 1, size / 3 - 4)
            t.right(90)
            edgeWithSpace(t, depth - 1, size / 3)
            t.right(90)
            edgeWithSpace(t, depth - 1, size / 3 - 4)
            t.left(90)
            edgeWithSpace(t, depth - 1, size / 3 - 4)
    return None


def edgeWithoutSpace(t, depth, size):
    """
        Function when called recursively draws the fractal antenna as a single line without space (touching)
        :param t: turtle object
        :param depth: level of fractal
        :param size: size of antenna
        :return: None
        :pre: (relative) pos (0,0) heading (East), pen down
        :post: (relative) pos (size, 0) heading (East), pen down
        """
    if depth == 0:
        t.forward(size)

        return
    else:
            edgeWithoutSpace(t, depth - 1, size / 3)
            t.left(90)
            edgeWithoutSpace(t, depth - 1, size / 3 )
            t.right(90)
            edgeWithoutSpace(t, depth - 1, size / 3)
            t.right(90)
            edgeWithoutSpace(t, depth - 1, size / 3)
            t.left(90)
            edgeWithoutSpace(t, depth - 1, size / 3)


def main():

    size = int(input("enter the size of the antenna"))
    depth = int(input("Enter the depth of the antenna"))

    print("Do you want to draw the antenna as a single path or sequence of squares")
    decision = int(input("1-->SinglePath / 2-->Sequence of squares)"))


    if  decision == 1:
        print("In single path, do you want the corners without touching?")
        cornernotouch = input("if yes enter Y else N ")

        if(cornernotouch == "n"):
            turtle.left(45)
            edgeWithoutSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithoutSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithoutSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithoutSpace(turtle, depth, size)
        else:
            turtle.left(45)
            edgeWithSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithSpace(turtle, depth, size)
            turtle.left(90)
            edgeWithSpace(turtle, depth, size)
    elif decision == 2:

        sizetemp = size/5**depth

        turtle.right(45)
        antenna(turtle,depth,sizetemp)

    turtle.exitonclick()

    turtle.mainloop()




if __name__ == '__main__':
        main()




