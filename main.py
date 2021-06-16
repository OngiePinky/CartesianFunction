import math
def input_x():
    x = int(input("Faka ikho-odineyithi ka x"))
    return x
def input_y():
    y = int(input("Faka kho-odineyithi ka y"))
    return y
def input_name():
    name = input("Faka igama lepoyinti")
    return name
def calc_distance(x, y):
    distance = math.sqrt((0-x)*(0-x) + (0-y)*(0-y))
    print("Idistensi phakathi kwa point 1 no point 2 yilena", distance)
    return distance
def reflect_y(x, y):
    x = x * (-1)
    print("reflected point is (", x, ",", y, ")")
    return x
def reflect_x(x, y):
    y = y * (-1)
    print("Reflected point is (", x, ",", y, ")")
    return y
def equation(x, y):
    gradient = (0-y)/(0-x)
    print("Equation: ", gradient, "x", "+", y)
    return gradient
def quadrant(x, y):

    if x < 0 and y > 0:
        print("NORTH WEST QUADRANT")
    if x > 0 and y > 0:
        print("NORTH EAST QUADRANT")
    if x < 0 and y < 0:
        print("SOUTH WEST QUADRANT")
    if x > 0 and y < 0:
        print("SOUTH WEST QUADRANT")

if __name__ == '__main__':
    xx = input_x()
    yy = input_y()
    nn = input_name()
    dd = calc_distance(xx, yy)
    rx = reflect_x(xx, yy)
    ry = reflect_y(xx, yy)
    equation(xx, yy)
    quadrant(xx, yy)

