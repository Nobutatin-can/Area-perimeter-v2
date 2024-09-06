# Ascii art
triangle = r"""
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
"""

rectangle = r"""
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
"""

square = r"""
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
"""

circle = r"""
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
 """

print(triangle, rectangle, square, circle)

