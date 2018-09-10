# Imports
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

# Variables
plane_amount = 0;
plane = True;
plane_position = [3, 8]

# LED colours
red = [150, 0, 0]
light_red = [255, 0, 0]

# Functions
def plane_nearby():
    plane = True
    plane_position[1] = 8
    
def draw_plane():
    # Update position
    plane_position[1] -= 1
    
    # Display plane
    if plane_position[1] <= 7 and plane_position[1] >= 0:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1], red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1], red)
    
    if plane_position[1] <= 6 and plane_position[1] >= -1:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 1, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 1, red)
        
    if plane_position[1] <= 5 and plane_position[1] >= -2:
        # Body
       sense.set_pixel(plane_position[0], plane_position[1] + 2, red)
       sense.set_pixel(plane_position[0] + 1, plane_position[1] + 2, red)
       
    if plane_position[1] <= 4 and plane_position[1] >= -3:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 3, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 3, red)
        
        # Left and Right wing
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 3, light_red)
        sense.set_pixel(plane_position[0] - 2, plane_position[1] + 3, light_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 3, light_red)
        sense.set_pixel(plane_position[0] + 3, plane_position[1] + 3, light_red)
        
    if plane_position[1] <= 3 and plane_position[1] >= -4:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 4, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 4, red)
        
        # Left and Right wing
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 4, light_red)
        sense.set_pixel(plane_position[0] - 2, plane_position[1] + 4, light_red)
        sense.set_pixel(plane_position[0] - 3, plane_position[1] + 4, light_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 4, light_red)
        sense.set_pixel(plane_position[0] + 3, plane_position[1] + 4, light_red)
        sense.set_pixel(plane_position[0] + 4, plane_position[1] + 4, light_red)
        
    if plane_position[1] <= 2 and plane_position[1] >= -5:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 5, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 5, red)
        
    if plane_position[1] <= 1 and plane_position[1] >= -6:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 6, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 6, red)
        
    if plane_position[1] <= 0 and plane_position[1] >= -7:
        # Body
        sense.set_pixel(plane_position[0], plane_position[1] + 7, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 7, red)
        
        # Left and Right tail
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 7, light_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 7, light_red)
        
    # Reset
    if plane_position[1] == -8:
        plane = False;
    
# Main program
while plane == True:
    sense.clear(0, 0 ,0)
    draw_plane()
    sleep(0.15)  