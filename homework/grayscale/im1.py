import sys
import stddraw
import luminance
from picture import Picture
import stdarray
import stdio

'''
im1.py
Kellan Stempin

Takes an image filename from the command line and returns a grayscale intensity histogram.
'''

#function gets the frequency of each grayscale intensity, and stores those frequencies in an array
def get_intensity(pic):
    frequencies = stdarray.create1D(256, 0) #256 0's to count each possible intensity (255+1)
    #loop through every pixel
    for col in range(pic.width()):
        for row in range(pic.height()):
            #get color components for each pixel and convert to grayscale intensity
            pixel = pic.get(col, row)
            gray_value = int(round(luminance.luminance(pixel)))
            #count how many times each value appears in the image
            #add 1 to the index of that value
            frequencies[gray_value] += 1
    return frequencies

#function to draw each line of the histogram            
def draw_histogram(frequencies):
    #set scales and canvas size
    stddraw.setCanvasSize(1024, 400)
    stddraw.setXscale(0, 256)
    stddraw.setYscale(0, max(frequencies) * 1.1)
    stddraw.setPenRadius(0.1)
    #draw each line
    for i in range(len(frequencies)):
        stddraw.line(i, 0, i, frequencies[i])

#take image filename as a commandline argument
pic = Picture(sys.argv[1])

#call functions and display the histogram
frequencies = get_intensity(pic)
draw_histogram(frequencies)
stdio.writeln(frequencies)
stddraw.show()


