import stdio, stdarray, sys, stddraw

'''
barcode.py
Kellan Stempin
'''

#create an array to store the encoding for each digit 1 = full height, 0 = half
codes = stdarray.create1D(10, '')
codes[0] = "11000"
codes[1] = "00011"
codes[2] = "00101"
codes[3] = "00110"
codes[4] = "01001"
codes[5] = "01010"
codes[6] = "01100"
codes[7] = "10001"
codes[8] = "10010"
codes[9] = "10100"

#constants for dimensions of each bar
BAR_WIDTH = 0.05
FULL_HEIGHT = 1.0
HALF_HEIGHT = 0.5


def draw_bar(x, height, color):
    '''draws a vertical bar with a given x position, height, and color'''
    stddraw.setPenColor(color)
    stddraw.filledRectangle(x, 0, BAR_WIDTH, height)


def bar_sequence(x, digit):
    '''draws the bar sequence for a given digit starting at a given x postiton'''
    draw_bar(x, FULL_HEIGHT, stddraw.WHITE)  #draw whitespawce after first guardbar
    x += BAR_WIDTH
    bars = codes[digit]
    #draw the 5 bars for a given digit, with white bars drawn in between
    for i in range(5):
        if bars[i] == '1':
            height = FULL_HEIGHT
        else:
            height = HALF_HEIGHT
        draw_bar(x, height, stddraw.BLACK)
        x += BAR_WIDTH
        draw_bar(x, height, stddraw.WHITE)
        x += BAR_WIDTH


def calc_checksum(zipcode):
    '''calculates the checksum digit for a given zipcode'''
    total = sum(int(digit) for digit in zipcode)
    return (10 - (total % 10)) % 10


def draw_barcode(zipcode):
    '''draws the barcode in its entirety for a given zipcode, checksum included'''
    zipcode = str(zipcode)
    checksum_digit = calc_checksum(zipcode)
    full_code = zipcode + str(checksum_digit)  #add zipcode and checksum for the full sequence
    total_bars = len(full_code) * 5 * 2 + 4  #calculate total bars for scaling
    stddraw.setXscale(0, total_bars * BAR_WIDTH)
    stddraw.setYscale(0, FULL_HEIGHT * 2)
    x = 0  #x coordinate starts at 0
    
    #draw the first guard bar and increment the x position
    draw_bar(x, FULL_HEIGHT, stddraw.BLACK)
    x += BAR_WIDTH
    
    #draw the full zipcode
    for digit in full_code:
        bar_sequence(x, int(digit))
        x += 5 * BAR_WIDTH * 2
    
    #draw the final guard bar
    draw_bar(x, FULL_HEIGHT, stddraw.WHITE)
    x += BAR_WIDTH
    draw_bar(x, FULL_HEIGHT, stddraw.BLACK)
    
    #display the barcode
    stddraw.show()

#test client
def main():
    zipcode = sys.argv[1]
    draw_barcode(zipcode)


if __name__ == "__main__":
    main()
