import sys
import stddraw
from picture import Picture

'''
im2.py
Kellan Stempin

Takea picture filename as a command line argument and flips it clockwise, horizontally
at 90 degrees.
'''

def rotate_pic(pic):
    #get original dimensions
    width = pic.width()
    height = pic.height()
    #flip rows and columns
    rotated = Picture(height, width)

    for col in range(width):
        for row in range(height):
            color = pic.get(col, row)
            rotated.set((height - row) - 1, col, color) #set flipped pixels (height - row for clockwise rotation)
    return rotated

#take filename as a command line argument
original = Picture(sys.argv[1])
#rotate image
rotated = rotate_pic(original)

#set scale and canvas size
stddraw.setCanvasSize(rotated.width(), rotated.height())
stddraw.setXscale(0, rotated.width())
stddraw.setYscale(0, rotated.height())

#center and draw the rotated image
stddraw.picture(rotated, rotated.width() / 2, rotated.height() / 2)
stddraw.show()
