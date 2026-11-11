import random
randRotCenter = random.choice([0, 90, 180, 270])
# Function definition for person 1 here
# Insert your name in the function name.
# Do not change anything else yet!
def draw_feifan_tile(t, x, y, size, rotation, palette, tile_type="center"):
 """
 Draws a parameterized geometric tile centered at (x, y).


 Parameters:
 - t: Turtle object
 - x, y (float/int): Center coordinates of the tile
 - size (float/int): Width and height of the tile bounding box
 - rotation (int): Orientation angle (0, 90, 180, 270)
 - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
 - tile_type (str): "center", "border", or "corner" (defaults to "center")
 """


 # ==========================================
 # TURTLE SETUP
 # ==========================================
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)


 # Useful relative dimension constants (derived from size)
 half = size / 2
 quarter = size / 4
 eighth = size / 8
 sixteenth = size / 16


 # ==========================================
 # BASE BACKGROUND
 # All tile variations share a clean backdrop
 # ==========================================
 # Move to the bottom-left corner relative to orientation
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)


 t.pencolor(palette["bg"])
 t.fillcolor(palette["bg"])
 t.pensize(2)
 t.pendown()
 t.begin_fill()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.end_fill()
 t.penup()


 # Return turtle to the true center of the tile
 t.jumpto(x, y)
 t.setheading(rotation)


 ######################### YOUR CHANGES START HERE ###########################


 # ==========================================
 # CONDITIONAL GEOMETRY (Based on tile_type)
 # ==========================================


  # ------------------------------------------
 # OPTION 1: CORNER TILE (Concentric Quarter Fan)
 # ------------------------------------------
 if tile_type == "corner":
     # 1. Concentric Quarter-Circles radiating from outer corner
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(-half)
     t.right(90)
     t.color(palette["primary"], palette["primary"])
     t.pensize(1)
     t.pendown()
     t.begin_fill()
     t.forward(quarter * 2.8)
     t.left(90)
     t.circle(quarter * 2.8, 90)
     t.left(90)
     t.forward(quarter * 2.8)
     t.end_fill()
     t.penup()
     # Middle quarter-circle in secondary
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(-half)
     t.right(90)
     t.color(palette["secondary"], palette["secondary"])
     t.pendown()
     t.begin_fill()
     t.forward(quarter * 1.8)
     t.left(90)
     t.circle(quarter * 1.8, 90)
     t.left(90)
     t.forward(quarter * 1.8)
     t.end_fill()
     t.penup()
     # Inner quarter-circle in accent
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(-half)
     t.right(90)
     t.color(palette["accent"], palette["accent"])
     t.pendown()
     t.begin_fill()
     t.forward(quarter * 0.9)
     t.left(90)
     t.circle(quarter * 0.9, 90)
     t.left(90)
     t.forward(quarter * 0.9)
     t.end_fill()
     t.penup()
     # Framing lines along the outer boundary
     t.pencolor(palette["accent"])
     t.pensize(3)
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(half)
     t.left(180)
     t.pendown()
     t.forward(size)
     t.left(90)
     t.forward(size)
     t.penup()
     # Inward-pointing star jewel
     t.jumpto(x, y)
     t.setheading(rotation + 45)
     t.forward(quarter * 0.8)
     t.dot(eighth * 1.2, palette["accent"])
     t.dot(sixteenth * 1.0, palette["primary"])
 # ------------------------------------------
 # OPTION 2: BORDER TILE (Scalloped Frieze)
 # ------------------------------------------
 elif tile_type == "border":
     # 1. Base runner stripe along bottom
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(-half)
     t.right(90)
     t.color(palette["primary"], palette["primary"])
     t.pensize(1)
     t.pendown()
     t.begin_fill()
     for _ in range(2):
         t.forward(size)
         t.left(90)
         t.forward(quarter * 0.7)
         t.left(90)
     t.end_fill()
     t.penup()
     # 2. Golden divider line
     t.pencolor(palette["accent"])
     t.pensize(3)
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(-half + quarter * 0.7)
     t.right(90)
     t.pendown()
     t.forward(size)
     t.penup()
     # 4. Inward linear accent stripe
     t.pencolor(palette["primary"])
     t.pensize(2)
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-half)
     t.left(90)
     t.forward(quarter * 0.6)
     t.right(90)
     t.pendown()
     t.forward(size)
     t.penup()
 # ------------------------------------------
 # OPTION 3: CENTER TILE (Celestial Sunburst)
 # ------------------------------------------
 else:
     # 1. 12-ray radiating Sunburst in primary
     for i in range(12):
         angle = i * 30
         t.jumpto(x, y)
         t.setheading(rotation + angle + randRotCenter)
         t.forward(quarter * 0.6)
         t.color(palette["primary"], palette["primary"])
         t.pendown()
         t.begin_fill()
         t.left(30)
         t.forward(quarter * 0.7)
         t.right(60)
         t.forward(quarter * 0.7)
         t.right(120)
         t.forward(quarter * 0.7)
         t.right(60)
         t.forward(quarter * 0.7)
         t.end_fill()
         t.penup()
         t.jumpto(x + quarter * 1.3, y + quarter * 1.3)
         t.dot(sixteenth * 0.8, palette["primary"])
         t.penup()
     # 2. Concentric ring in secondary
     t.jumpto(x, y)
     t.setheading(rotation + randRotCenter)
     t.forward(quarter * 0.8)
     t.left(90)
     t.pencolor(palette["secondary"])
     t.pensize(4)
     t.pendown()
     t.circle(quarter * 0.8)
     t.penup()
     # 3. Inner 8-pointed star in secondary
     for offset in [45, 0]:
         t.jumpto(x, y)
         t.setheading(rotation + offset + randRotCenter)
         t.forward(quarter * 0.5)
         t.left(135)
         t.color(palette["secondary"], palette["secondary"])
         t.pendown()
         t.begin_fill()
         for _ in range(4):
             t.forward(quarter * 0.5 * 1.414)
             t.left(90)
         t.end_fill()
         t.penup()
     # 4. Center sun medallion in accent
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(eighth * 0.7)
     t.left(90)
     t.color(palette["accent"], palette["accent"])
     t.pendown()
     t.begin_fill()
     t.circle(eighth * 0.7)
     t.end_fill()
     t.penup()
     # 5. Bullseye center dots
     t.jumpto(x, y)
     t.dot(eighth * 0.7, palette["primary"])
     t.dot(sixteenth * 0.8, palette["bg"])
     t.penup()
     t.jumpto(x + quarter * 1.3, y + quarter * 1.3)
     t.dot(sixteenth * 0.8, palette["primary"])
     t.penup()
   
  
 # ==========================================
 # DRAW BORDER (OUTLINE AROUND TILE)
 # ==========================================
 t.pencolor(palette["primary"])
 t.pensize(2)
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)
 t.pendown()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.penup()
 ######################### YOUR CHANGES END HERE #############################


 # ==========================================
 # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
 # ==========================================


 ############## This part is my own drawing #######################
 ################## Change it to your design ######################
 t.pencolor(palette["secondary"])
 t.pensize(2)


 # Go to the corner
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)


 # Draw the border
 t.pendown()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.penup()


 ######################### YOUR CHANGES END HERE #############################


 # ==========================================
 # TURTLE TEARDOWN
 # Reset pen, heading, and state for the next user
 # ==========================================
 t.penup()
 t.setheading(0)
 t.pencolor((0, 0, 0))


# Function definition for person 2 here




# Function definition for person 2 here
def draw_riley_tile(t, x, y, size, rotation, palette, tile_type="center"):
 
 # ==========================================
 # TURTLE SETUP
 # ==========================================
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 
 
 
 
 # Useful relative dimension constants (derived from size)
 half = size / 2
 quarter = size / 4
 
 
 
 
 # ==========================================
 # BASE BACKGROUND
 # All tile variations share a clean backdrop
 # ==========================================
 # Move to the bottom-left corner relative to orientation
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)
 
 
 
 
 t.pencolor(palette["bg"])
 t.fillcolor(palette["bg"])
 t.pensize(2)
 t.pendown()
 t.begin_fill()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.end_fill()
 t.penup()
 
 
 
 
 # Return turtle to the true center of the tile
 t.jumpto(x, y)
 t.setheading(rotation)




######################### YOUR CHANGES START HERE ###########################




# ==========================================
# CONDITIONAL GEOMETRY (Based on tile_type)
# ==========================================




# ------------------------------------------
# OPTION 1: CORNER TILE
# ------------------------------------------
 if tile_type == "corner":
 
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
     t.pencolor(palette["accent"])
     t.pensize(3)
     t.forward(quarter)
     t.right(90)
     t.forward(quarter)
     t.left(180)
 
 
 
 
     t.pendown()
     t.forward(half)
     t.left(90)
     t.forward(half)
     t.penup()
 
 
 
 
     t.jumpto(x, y)
     t.setheading(rotation)
     t.color(palette["primary"], palette["primary"])
     t.forward(quarter + quarter / 2)
     t.left(90)
     t.forward(quarter)
 
 
 
 
     t.pendown()
     t.begin_fill()
     t.dot(quarter / 2)
     t.end_fill()
     t.left(90)
     t.forward(quarter / 2)
     t.color(palette["secondary"])
     t.dot(quarter / 4)
     t.penup()
 
 
 
 
 # ------------------------------------------
 # OPTION 2: BORDER TILE
 # ------------------------------------------
 elif tile_type == "border":
 
 
 
 
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
     t.color(palette["primary"], palette["primary"])
     t.forward(-half)
     t.left(90)
     t.forward(quarter)
     t.right(90)
 
 
 
 
     t.pendown()
     t.begin_fill()
     for _ in range(2):
         t.forward(size)
         t.left(90)
         t.forward(quarter)
         t.left(90)
     t.end_fill()
     t.penup()
 
 
 
 
     t.jumpto(x, y)
     t.setheading(rotation)
     t.pencolor(palette["accent"])
     t.pensize(3)
     t.forward(-half)
     t.pendown()
     t.forward(size)
     t.penup()
 
 
 
 
 # ------------------------------------------
 # OPTION 3: CENTER TILE
 # ------------------------------------------
 else:
 
 
 
 
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
 
 
 
 
   #i want polka dots of primary color behind
   #spiderweb in secondary color
   #spider in accent color
 
 
 
 
   # ------- polka dots ---------
   t.pencolor(palette["primary"])
   spacing = 12
   thisSpacing = spacing
   margin = 10
   xMargin = 9
   yMargin = 12
   t.jumpto(-x - half + xMargin + 1, y + half - yMargin)
   ySpace = y + half - yMargin
   i = 0
   while i < 9:
     ii = 0
     while ii < 11:
       #drawing row of dots
       #t.dot(5);
       t.jumpto(-x - half + xMargin + thisSpacing, ySpace)
       thisSpacing += 10
       ii += 1
     #reset spacing
     thisSpacing = spacing
     #moving y down by spacing
     ySpace = ySpace - spacing
     t.jumpto(x - half + xMargin + 1, ySpace)
     i += 1
 
 
 
 
   #-------- spider web ----------
   t.pencolor(palette["secondary"])
 
 
 
 
   import math
   t.speed(0)
   #size=200
   spiderSize = size / 2
 
 
 
 
   t.jumpto(x,y)
   t.setheading(rotation + 90) #Point the top
   for i in range(0,6):
     t.forward(spiderSize)
     t.penup()
     t.forward(-spiderSize)
     t.left(60)
     t.pendown()
 
 
 
 
   #t.jumpto(x,y)
   t.setheading(rotation + 90) #Point the top
   t.forward(spiderSize)
   t.setheading(rotation + 215) #Point the left
   newSize=spiderSize
   newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
   for i in range(0,30):
     t.forward(newSize)
     t.left(60)
     newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))
 
 
 
 
   #---- spider ----
   t.pencolor(palette["accent"])
   t.jumpto(x+15,y+5)
   t.dot(7)
   #top upward legs
   thisX = t.xcor()
   thisY = t.ycor()
   t.goto(thisX-10,thisY+10)
   t.jumpto(thisX,thisY)
   t.goto(thisX+10,thisY+10)
 
 
 
 
   #top straight leg
   t.jumpto(thisX,thisY)
   t.goto(thisX-10,thisY)
   t.jumpto(thisX,thisY)
   t.goto(thisX+10,thisY)
 
 
 
 
 
 
 
 
   t.jumpto(x+15,y-2)
   t.dot(8)
   #bottom outward leg
   thisX = t.xcor()
   thisY = t.ycor()
   t.goto(thisX-10,thisY-10)
   t.jumpto(thisX,thisY)
   t.goto(thisX+10,thisY-10)
 
 
 
 
   #bottom straight leg
   t.jumpto(thisX,thisY)
   t.goto(thisX-10,thisY)
   t.jumpto(thisX,thisY)
   t.goto(thisX+10,thisY)
 
 
 
 
 
 
 # ==========================================
 # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
 # ==========================================
 
 
 
 
 ############## This part is my own drawing #######################
 ################## Change it to your design ######################
 t.pencolor(palette["secondary"])
 t.pensize(2)
 
 
 
 
 # Go to the corner
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)
 
 
 
 
 # Draw the border
 t.pendown()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.penup()
 
 
 
 
 ######################### YOUR CHANGES END HERE #############################
 
 
 
 
 # ==========================================
 # TURTLE TEARDOWN
 # Reset pen, heading, and state for the next user
 # ==========================================
 t.penup()
 t.setheading(0)
 t.pencolor((0, 0, 0))
 
 
 # Function definition for person 3 here
 

def draw_melody_tile(t, x, y, size, randRotCenter, palette, tile_type="center"):
 
 # ==========================================
 # TURTLE SETUP
 # ==========================================
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 
 
 
 
 # Useful relative dimension constants (derived from size)
 half = size / 2
 quarter = size / 4
 
 
 
 
 # ==========================================
 # BASE BACKGROUND
 # All tile variations share a clean backdrop
 # ==========================================
 # Move to the bottom-left corner relative to orientation
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)
 
 
 
 
 t.pencolor(palette["bg"])
 t.fillcolor(palette["bg"])
 t.pensize(2)
 t.pendown()
 t.begin_fill()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.end_fill()
 t.penup()
 
 
 
 
 # Return turtle to the true center of the tile
 t.jumpto(x, y)
 t.setheading(rotation)
 
 
 
 
 ######################### YOUR CHANGES START HERE ###########################
 
 
 
 
 # ==========================================
 # CONDITIONAL GEOMETRY (Based on tile_type)
 # ==========================================
 
 
 
 
 # ------------------------------------------
 # OPTION 1: CORNER TILE
 # ------------------------------------------
 if tile_type == "corner":
 
 
 
 
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
 
 
     t.penup()
     t.jumpto(x + half * 0.48, y + half * 0.48)
     t.setheading(rotation + 45)
     t.color(palette["primary"], palette["primary"])
     t.pendown()
     t.begin_fill()
     for _ in range(4):
         t.forward(quarter * 0.65)
         t.left(90)
     t.end_fill()
     t.penup()
 
 
     t.jumpto(x + half * 0.48, y + half * 0.48)
     t.setheading(rotation + 45)
     t.forward(quarter * 0.12)
     t.color(palette["accent"], palette["accent"])
     t.pendown()
     t.begin_fill()
     for _ in range(4):
         t.forward(quarter * 0.4)
         t.left(90)
     t.end_fill()
     t.penup()
 
 
     t.pencolor(palette["secondary"])
     t.pensize(2)
     for i in range(2):
         t.jumpto(x + half * 0.48, y + half * 0.48)
         t.setheading(rotation + 180 + i * 90)
         t.forward(quarter * 0.25)
         t.pendown()
         t.circle(quarter * 0.25, 90)
         t.penup()
 
 
     t.dot(quarter * 0.18, palette["accent"])
     t.jumpto(x + half * 0.48, y + half * 0.22)
     t.dot(quarter * 0.12, palette["secondary"])
     t.jumpto(x + half * 0.22, y + half * 0.48)
     t.dot(quarter * 0.12, palette["secondary"])
 
 
 
 
 # ------------------------------------------
 # OPTION 2: BORDER TILE
 # ------------------------------------------
 elif tile_type == "border":
 
 
 
 
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
 
 
     # Keep all decorations relative to the tile's center
     band_width = size * 0.85
     band_height = quarter * 0.7
     diamond_size = quarter * 0.2
 
 
     t.penup()
     t.jumpto(x, y)
     t.setheading(rotation)
     t.forward(-band_width / 2)
     t.left(90)
     t.forward(-band_height / 2)
     t.right(90)
 
 
     t.color(palette["primary"], palette["primary"])
     t.pendown()
     t.begin_fill()
     for _ in range(2):
         t.forward(band_width)
         t.left(90)
         t.forward(band_height)
         t.left(90)
     t.end_fill()
     t.penup()
 
 
     for offset in [-band_height * 0.4, band_height * 0.4]:
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation)
         t.forward(-band_width / 2)
         t.left(90)
         t.forward(offset)
         t.right(90)
         t.pencolor(palette["accent"])
         t.pensize(2)
         t.pendown()
         t.forward(band_width)
         t.penup()
 
 
     for i in range(5):
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation)
         t.forward(-band_width / 2 + band_width * (i + 0.5) / 5)
 
 
         t.color(palette["accent"], palette["accent"])
         t.pendown()
         t.begin_fill()
         t.left(45)
         for _ in range(4):
             t.forward(diamond_size)
             t.left(90)
         t.end_fill()
         t.penup()
 
 
         for offset in [-band_height * 0.28, band_height * 0.28]:
             t.penup()
             t.jumpto(x, y)
             t.setheading(rotation)
             t.forward(-band_width / 2 + band_width * (i + 0.5) / 5)
             t.left(90)
             t.forward(offset)
             t.dot(quarter * 0.07, palette["secondary"])
 
 
 
 
 
 
 # ------------------------------------------
 # OPTION 3: CENTER TILE
 # ------------------------------------------
 else:
   ############## This part is my own drawing #######################
   ################## Change it to your design ######################
     t.pencolor(palette["secondary"])
     t.pensize(2)
 
 
     for i in range(8):
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation + i * 45 + randRotCenter)
         t.forward(quarter * 0.35)
         t.pendown()
         t.circle(quarter * 0.45, 180)
         t.penup()
 
 
     for i in range(8):
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation + i * 45 + 22.5 + randRotCenter)
         t.forward(quarter * 0.22)
         t.color(palette["primary"])
         t.pendown()
         t.circle(quarter * 0.25, 180)
         t.penup()
 
 
     t.jumpto(x, y)
     t.dot(quarter * 0.65, palette["accent"])
 
 
     t.jumpto(x, y)
     t.dot(quarter * 0.28, palette["secondary"])
 
 
     for i in range(8):
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation + i * 45 + randRotCenter)
         t.forward(quarter * 1.15)
         t.pencolor(palette["accent"])
         t.pendown()
         t.forward(quarter * 0.18)
         t.penup()
 
 
     for i in range(4):
         t.penup()
         t.jumpto(x, y)
         t.setheading(rotation + i * 90 + 45 + randRotCenter)
         t.forward(quarter * 1.05)
         t.setheading(rotation + i * 90 + 45)
         t.color(palette["primary"], palette["primary"])
         t.pendown()
         t.begin_fill()
         for _ in range(4):
             t.forward(quarter * 0.2)
             t.left(90)
         t.penup()
         t.jumpto(x + quarter * 1.3, y + quarter * 1.3)
         t.dot(quarter * 0.4, palette["primary"])
         t.end_fill()
    
 
 # ==========================================
 # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
 # ==========================================
 
 
 
 
 ############## This part is my own drawing #######################
 ################## Change it to your design ######################
 t.pencolor(palette["secondary"])
 t.pensize(2)
 
 
 
 
 # Go to the corner
 t.penup()
 t.jumpto(x, y)
 t.setheading(rotation)
 t.forward(-half)
 t.left(90)
 t.forward(-half)
 t.right(90)
 
 
 
 
 # Draw the border
 t.pendown()
 for _ in range(4):
     t.forward(size)
     t.left(90)
 t.penup()
 
 
 
 
 ######################### YOUR CHANGES END HERE #############################
 
 
 
 
 # ==========================================
 # TURTLE TEARDOWN
 # Reset pen, heading, and state for the next user
 # ==========================================
 t.penup()
 t.setheading(0)
 t.pencolor((0, 0, 0))
