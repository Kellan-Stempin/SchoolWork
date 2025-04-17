import stdio
import stddraw
import sys
import math

'''
recursierpinsky.py
Kellan Stempin
'''

#function for drawing the triangles
def draw_triangle(x0, y0, x1, y1, x2, y2):
    stddraw.line(x0, y0, x1, y1)
    stddraw.line(x1, y1, x2, y2)
    stddraw.line(x2, y2, x0, y0)

#recursive function that takes the midpoint of each line and starts a new triangle
#3 per iteration
def draw(n, x0, y0, x1, y1, x2, y2):
    if n == 0:
        return
    else:
        #find the middle of each line
        midx0 = (x0 + x1) / 2
        midy0 = (y0 + y1) / 2
        midx1 = (x1 + x2) / 2
        midy1 = (y1 + y2) / 2
        midx2 = (x2 + x0) / 2
        midy2 = (y2 + y0) / 2

        #draw new triangle
        draw_triangle(midx0, midy0, midx1, midy1, midx2, midy2)

        #call the function 3 times per iteration (3 triangles)
        draw(n - 1, x0, y0, midx0, midy0, midx2, midy2)
        draw(n - 1, midx0, midy0, x1, y1, midx1, midy1)
        draw(n - 1, midx2, midy2, midx1, midy1, x2, y2)

#take the number of iterations as an integer
n = int(sys.argv[1])
stddraw.setCanvasSize(800,800)
stddraw.setPenRadius(0.0)

#draw the original triangle
draw_triangle(0, 0, 1, 0, 0.5, math.sqrt(3)/ 2)
#call 
draw(n, 0, 0, 1, 0, 0.5, math.sqrt(3)/2)

stddraw.show()