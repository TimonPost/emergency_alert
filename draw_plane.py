# Imports
from sense_hat import SenseHat
sense = SenseHat()
from time import sleep

# Variables
plane = True;
frame = 0;
plane_x = 3;
plane_position = [3, 7]
red = [255, 0, 0]
dark_red = [255, 200, 100]

# Functions
sense.clear()
def draw_plane():
    # Update position
    plane_position[1] -= 1
    # Body
    if plane_position[1] <= 7 and plane_position[1] >= 0:
        sense.set_pixel(plane_position[0], plane_position[1], red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1], red)
    
    if plane_position[1] <= 6 and plane_position[1] >= -1:
        sense.set_pixel(plane_position[0], plane_position[1] + 1, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 1, red)
        
    if plane_position[1] <= 5 and plane_position[1] >= -2:
       sense.set_pixel(plane_position[0], plane_position[1] + 2, red)
       sense.set_pixel(plane_position[0] + 1, plane_position[1] + 2, red)
       
    if plane_position[1] <= 4 and plane_position[1] >= -3:
        sense.set_pixel(plane_position[0], plane_position[1] + 3, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 3, red)
        
        # Left and Right wing
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 3, dark_red)
        sense.set_pixel(plane_position[0] - 2, plane_position[1] + 3, dark_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 3, dark_red)
        sense.set_pixel(plane_position[0] + 3, plane_position[1] + 3, dark_red)
        
    if plane_position[1] <= 3 and plane_position[1] >= -4:
        sense.set_pixel(plane_position[0], plane_position[1] + 4, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 4, red)
        
        # Left and Right wing
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 4, dark_red)
        sense.set_pixel(plane_position[0] - 2, plane_position[1] + 4, dark_red)
        sense.set_pixel(plane_position[0] - 3, plane_position[1] + 4, dark_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 4, dark_red)
        sense.set_pixel(plane_position[0] + 3, plane_position[1] + 4, dark_red)
        sense.set_pixel(plane_position[0] + 4, plane_position[1] + 4, dark_red)
        
    if plane_position[1] <= 2 and plane_position[1] >= -5:
        sense.set_pixel(plane_position[0], plane_position[1] + 5, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 5, red)
        
    if plane_position[1] <= 1 and plane_position[1] >= -6:
        sense.set_pixel(plane_position[0], plane_position[1] + 6, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 6, red)
        
    if plane_position[1] <= 0 and plane_position[1] >= -7:
        sense.set_pixel(plane_position[0], plane_position[1] + 7, red)
        sense.set_pixel(plane_position[0] + 1, plane_position[1] + 7, red)
        
        # Left and Right tail
        sense.set_pixel(plane_position[0] - 1, plane_position[1] + 7, dark_red)
        sense.set_pixel(plane_position[0] + 2, plane_position[1] + 7, dark_red)
        
    if plane_position == -8:
        plane = False;
        plane_postion[1] = 7

    
# Main program
while plane == True:
    sense.clear(0, 0 ,0)
    draw_plane()
    sleep(0.20)  