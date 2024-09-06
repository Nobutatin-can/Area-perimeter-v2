# Function for storing multiple line text
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

big_text("purple")



