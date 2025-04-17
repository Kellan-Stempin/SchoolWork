import sys
import stddraw
from picture import Picture
from color import Color

'''
im3.py
Kellan Stempin

Takes an image filename from the command line, returns 3 copies of that image
with only the red, green, or blue components.
'''
#function takes the picture as well as color_type(r, g or b) as arguments
def get_colors(pic, color_type):
    #get picture dimentions
    width = pic.width()
    height = pic.height()
    result = Picture(width, height)

    for col in range(width):
        for row in range(height):
            #get color components
            pixel = pic.get(col, row)
            r = pixel.getRed()
            g = pixel.getGreen()
            b = pixel.getBlue()

            #set color components
            if color_type == 'r':
                result.set(col, row, Color(r, 0, 0))
            elif color_type == 'g':
                result.set(col, row, Color(0, g, 0))
            elif color_type == 'b':
                result.set(col, row, Color(0, 0, b))
    #return a fully red, green, or blue image
    return result

#take picture filename as command line argument
original = Picture(sys.argv[1])

#call function 3 times for each color
red_pic = get_colors(original, 'r')
green_pic = get_colors(original, 'g')
blue_pic = get_colors(original, 'b')

#set canvas dimentions and scale
width = original.width()
height = original.height()
stddraw.setCanvasSize(width * 3, height)
stddraw.setXscale(0, width * 3)
stddraw.setYscale(0, height)

#center each image side by side
stddraw.picture(red_pic, width * 0.5, height / 2)
stddraw.picture(green_pic, width * 1.5, height / 2)
stddraw.picture(blue_pic, width * 2.5, height / 2)

stddraw.show()
