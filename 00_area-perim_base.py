# Libraries
import pandas

# Functions

# To store text that goes over many lines
def big_text(text):

    if text == "instructions":
        print('''\n
***** Instructions *****
          
Insert instructions here

**** Program Launched! ****''')
        
    elif text == "triangle":
        print(r"""
                        -                                                                            
                       /|\                                                                           
                      / | \                                                                          
                     /  |  \                                                                         
                    /   |   \                                                                        
                   /    |    \                                                                      
                  /     |     \                                                                      
                 /      |      \                                                                     
        Side 3  /       |       \ Side 2                                                             
               /        |        \                                                                   
              /         |         \                                                                  
             /          |          \                                                                 
            /           |           \                                                                
           /            |            \                                                               
          /             |             \                                                              
         /              |              \                                                             
        /               | Height        \                                                            
       /                |                \                                                           
      /                 |                 \                                                          
     /                  |                  \                                                         
    /                   |_____              \                                                        
   /                    |     |              \                                                       
  /                     |     |               \                                                      
 /                      |     |                \                                                     
/-----------------------------------------------\  
 <--------------- Base / Side 1 --------------->
""")
        
    elif text == "rectangle":
        print(r"""
+-----------------------------+                                                                           
|                             |  ^                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  L                                                                         
|                             |  e                                                                         
|                             |  n                                                                         
|                             |  g                                                                         
|                             |  h                                                                         
|                             |  t                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  |                                                                         
|                             |  v                                                                         
+-----------------------------+                                                                           
 <-----------Width-----------> 
""")
        
    elif text == "square":
        print(r"""
<-------------------Side-------------------->                                                                    
+-------------------------------------------+                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
|                                           |                                                                    
+-------------------------------------------+  
""")
        
    elif text == "circle":
        print(r"""
     Cercumference      ooo OOO OOO ooo                                                                    
         <          oOO                 OOo                                                                
      (   )     oOO                         OOo                                                            
       >     oOO                               OOo                                                         
           oOO                                   OOo                                                       
         oOO                                       OOo                                                     
        oOO                                         OOo                                                    
       oOO                                           OOo                                                   
      oOO                               Radius        OOo                                                  
      oOO                       <-------------------> OOo                                                  
      oOO----------------------0----------------------OOo                                                  
      oOO                  Diameter                   OOo                                                  
      oOO                                             OOo                                                  
       oOO                                           OOo                                                   
        oOO                                         OOo                                                    
         oOO                                       OOo                                                     
           oOO                                   OOo                                                       
             oOO                                OOo                                                         
                oOO                         OOo                                                            
                    oOO                 OOo                                                                
                        ooo OOO OOO ooo                                                                    
 """)
        
    else:
        print("!!!!!!!!!!YOU TYPED THE PARAMETER WRONG!!!!!!!!!!")  

    return 

# User response checker
def string_checker(question, num_letters, valid_responses, error):

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
            
        print(error)

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

# Main routine
        
# Valid responses lists
yes_no_list = ["yes", "no"]
shape_list = ["triangle", "square", "rectangle", "circle"]

# Briefly explain program
print("This program is for calculating the area and perimeter of some 2d shapes")

# Ask user if they want to see the instructions
see_instructions = string_checker("Do you want to see the instructions? :", 1, yes_no_list, "Please enter 'yes' or 'no'." )
if see_instructions == "yes":
    big_text("instructions")

# Ask user for the shape they want to calculate  
shape = string_checker("What shape do you want to calculate? :", 1, shape_list, "Please enter a valid shape.")

