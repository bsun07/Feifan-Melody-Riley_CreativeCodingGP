from ColabTurtlePlus.Turtle import *
import numpy as np
import random
import PIL
from PIL import Image
import matplotlib
from tilecollection import *
from palettes import *

smallsize = (400, 400)
my_picture = Image.open("ExamplePoster.png")
downsized_pic = my_picture.resize(smallsize)
display(downsized_pic)

tile_functions = [draw_feifan_tile, draw_riley_tile, draw_melody_tile]
# Create one function to handle everything
def generate_poster():

    title_text = input("Enter a title for your poster: ")
    
    nrows = int(input("Grid height: "))
    while nrows < 3 or nrows > 8:
        print("Should be between 3 and 8.")
        nrows = int(input("Grid height "))
    
    
    ncols = int(input("Grid width: "))
    while ncols < 3 or ncols > 8:
        print("Should be between 3 and 8.")
        ncols = int(input("Grid width "))
    
    p_name = input("Enter the name of the color palette you wish to use: ").lower()
    while p_name not in palette_names:
      print(f"Invalid palette name. The valid names are {palette_names}.")
      p_name = input("Enter the name of the color palette you wish to use: ").lower()
    
    print(f"You have selected the {p_name} palette.")
    
    if p_name == "random":
      print("Now generating a random color palette...")
      palette = {}
    
      for key in ["bg", "primary", "secondary", "accent"]:
        r = np.random.randint(256)
        g = np.random.randint(256)
        b = np.random.randint(256)
        palette[key] = (r, g, b)
    else:
     palette = palette_options[p_name]
    
    print("Success! Now generating your poster...")
    
    screen_width = 900
    screen_height = 900
    
    horizontal_spacing = 30
    vertical_spacing_above = 120
    vertical_spacing_below = 120
    
    size_horizontal = (screen_width - horizontal_spacing * 2) / ncols
    size_vertical = (screen_height - vertical_spacing_above - vertical_spacing_below) / nrows
    
    size = min(size_horizontal, size_vertical) * 0.8
    
    clearscreen()
    setup(screen_width, screen_height)
    t = Turtle()
    t.speed(0)
    t.jumpto(0, -250)
    
    #colors = list(palette.values())
    #if colors:
    #   palette.setdefault("bg", colors[0])
    #    palette.setdefault("primary", colors[1] if len(colors) > 1 else colors[0])
    #    palette.setdefault("secondary", colors[2] if len(colors) > 2 else colors[0])
    #    palette.setdefault("accent", colors[3] if len(colors) > 3 else colors[0])
    
    
    y_offset = screen_height / 2 - 100 - size / 2
    x_offset = size * (ncols - 1) / 2
    for row in range(nrows):
      y = y_offset - row * size
      for col in range(ncols):
        x = x_offset - col * size
        F = tile_functions[np.random.randint(len(tile_functions))]
        randRotCenter = random.choice([180, 90, 0, 270])
        randRotUpDown = random.choice([180, 0])
        randRotLR = random.choice([90, 270])
        #corners
        if row == 0 and col == 0: # TOP RIGHT
          F(t, x, y, size, 0, palette, "corner")
          tile_type = "corner"
          rotation = 0
        elif row == 0 and col == ncols - 1: #TOP LEFT
          F(t, x, y, size, 90, palette, "corner")
          tile_type = "corner"
          rotation = 90
        elif row == nrows - 1 and col == 0: #BOTTOM RIGHT
          F(t, x, y, size, 270, palette, "corner")
          tile_type = "corner"
          rotation = 270
        elif row == nrows - 1 and col == ncols - 1: #BOTTOM LEFT
          F(t, x, y, size, 180, palette, "corner")
          tile_type = "corner"
          rotation = 180
        elif row == 0 and (col != 0 and col != ncols): #TOP
           F(t, x, y, size, randRotUpDown, palette, "border")
           tile_type = "border"
           rotation = randRotUpDown
        elif row == nrows - 1 and (col != 0 and col != ncols): #BOTTOM
          F(t, x, y, size, randRotUpDown, palette, "border")
          tile_type = "border"
          rotation = randRotUpDown
        elif col == 0 and (row != 0 and row != nrows): #RIGHT
          F(t, x, y, size, randRotLR, palette, "border")
          tile_type = "border"
          rotation = randRotLR
        elif col == ncols - 1 and (row != 0 and row != nrows): #LEFT
          F(t, x, y, size, randRotLR, palette, "border")
          tile_type = "border"
          rotation = randRotLR
        # elif row == ncols - 1 and (col != 0 and col != nrows):
        #    tile_type = "border"
        #    rotation = 0
        # # #if left side border
        # elif col == 0 and (row != 0 and row != ncols):
        #   tile_type = "border"
        #   rotation = 0
        # #right side border
        # elif col == nrows - 1 and (row != 0 and row != nrows):
        #   tile_type = "border"
        #   rotation = 0
        else:
           F(t, x, y, size, randRotCenter, palette, "center")
           tile_type = "center"
           rotation = randRotCenter
        #F(t, x, y, size, rotation, palette, tile_type)
    
    grid_bottom_y = y_offset - nrows * size
    
    # title
    t.pendown()
    t.setheading(0)
    t.jumpto(0, -255)
    t.pencolor(list(palette.values())[0])
    t.write(title_text, align="center", font=("Arial", 50, "bold"))
    
    # credits / names
    t.penup()
    t.jumpto(0, grid_bottom_y - 65)
    t.pendown()
    t.jumpto(0, -280)
    #sentence
    t.write("by feifan, melody, riley", align="center", font=("Arial", 16, "bold"))
    
    t.jumpto(-225, -400)
    # Loop through all key, value pairs in the color palette dictionary.
    for label, rgb_value in palette.items():
    
      # Set the line color and the fill color.
      t.color(rgb_value, rgb_value)
    
      # Draw and fill the hexagon.
      t.pendown()
      t.begin_fill()
      for i in range(6):
        t.forward(60)
        t.left(60)
      t.end_fill()
    
      # Write the label.
      t.penup()
      t.right(90)
      t.forward(20)
      t.left(90)
      t.forward(30)
      t.write(rgb_value, align="center", font=("Arial", 16, "bold"))
    
      # Prepare for the next hexagon.
      t.forward(100)
      t.left(90)
      t.forward(20)
      t.right(90)
    
    t.hideturtle()
    t.done()
    
    saveSVG("/content/poster.svg")
