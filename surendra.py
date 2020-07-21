import turtle 
    
      
t = turtle.Turtle() 
  
# radius of the circle 
r = 40
  
# Loop for printing concentric circles 
for i in range(4): 
    t.circle(r * i) 
    t.up() 
    t.sety((r * i)*(-1)) 
    t.down() 
print("Boney here!")
