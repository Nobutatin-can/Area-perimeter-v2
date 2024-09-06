# Number checker for floats (can be n/a)
def num_check(question, can_null):

    valid = False
    while not valid:

        response = input(question)

        try:
            response = float(response)
            if response <=  0:
                print("This must be a number more than 0")

            else:
                return response
       
        except ValueError:

            if can_null == 1 and response == "n/a":
                return response
            
            else:
                print("this is an error")

# Square (Width)
width = num_check("What is the width? :", 0)    # Can't solve if n/a
print("Preimeter = {} | Area = {}". format(width*4, width*width))

# Rectangle (Length, width)
length = num_check("What is the length? :", 0)  # Can't solve if n/a
width = num_check("What is the width? :", 0)

# Circle (Diameter, radius, cercumference)
diameter = num_check("What is the diameter? :", 1)  # Need at least 1 to solve
radius = num_check("What is the radius? :", 1)
cercumference = num_check("What is the cercumference? :", 1)


# Triangle (Base, Hight, Side2, Side3)
base = num_check("What is the base length? :", 0)   # To solve area need Base and hight, for perimeter, base, side2 and side3
hight = num_check("What is the hight? :", 1)
side2 = num_check("How long is side 2? :", 1)
side3 = num_check("How long is side 3? :", 1)

try:
    area = 0.5 * base * hight
    print("area = {}".format(area))

except TypeError:
    print("error")

try:
    perimeter = base + side2 + side3
    print("area = {}".format(perimeter))

except TypeError:
    print("error")
