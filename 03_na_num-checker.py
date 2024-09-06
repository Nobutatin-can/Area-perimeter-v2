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
                print(response)
                return response
       
        except ValueError:

            if can_null == 1 and response == "n/a":
                return response
            
            else:
                print("this is an error")

# Main 
            
# Testing loop
while not False:
    can_na = num_check("Number can be n/a", 1)
    cant_na = num_check("Number can not be n/a", 0)



