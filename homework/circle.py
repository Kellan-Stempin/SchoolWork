'''
Kellan Stempin
circle.py
'''
import stdio
import stddraw
import stdarray
import sys
import math
import random
#set scale -1 = 1 so midpoint of circle is (0,0)
#start with drawing points on the circle
#360 degrees in a circle
#if we want 6 points each angle would be 60 degrees
#store x/y values in a 2d array
#take arguments for number of points and probability
n = int(sys.argv[1])
p = float(sys.argv[2])
#set the canvas sice and scale
stddraw.setCanvasSize(800, 800)
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)
stddraw.circle(0, 0, 1)
#colors for the random color option
colors = [
 stddraw.RED, stddraw.BLUE, stddraw.GREEN, stddraw.YELLOW,
 stddraw.ORANGE, stddraw.CYAN, stddraw.MAGENTA, stddraw.BLACK,
 stddraw.GRAY
]
#take angle to draw the point at in degrees
angle_increment = 360.0 / n
points = stdarray.create2D(n, 2, 0.0)
#calculate location of the first point and repeat n times
#also adding the points to the 2d array
for i in range(n):
    angle = angle_increment * i
    pointx = math.cos(math.radians(angle))
    pointy = math.sin(math.radians(angle))
    points[i][0] = pointx
    points[i][1] = pointy
    stddraw.point(pointx, pointy)
stddraw.setPenRadius(0.0)
#compare probability to a random float between 0-1
#if the probability passes draw the line between points
for i in range(n):
 for c in range(i + 1, n):
    if p >= random.random():
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[c][0]
        y2 = points[c][1]
        #random_color = random.choice(colors) #random colors option
        #stddraw.setPenColor(random_color)
        stddraw.line(x1, y1, x2, y2)
stddraw.show()