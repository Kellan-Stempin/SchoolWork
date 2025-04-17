import stddraw
import random 

'''
racecar.py
Kellan Stempin
'''

stddraw.setXscale(0,1)
stddraw.setYscale(0, 1)

#set the cars x and y values
car1x = 0.0
car1y = .75

car2x = 0.0
car2y = .25

#start the loop
while True:
    stddraw.clear()
    #add green background
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledSquare(0.0, 1.0, 5)

    #draw the road
    stddraw.setPenColor(stddraw.DARK_GRAY)
    stddraw.filledRectangle(0.0, 0.1, 1.0, .8)

    #draw the red car
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledCircle(car1x, car1y, .05)

    #draw the blue car
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledCircle(car2x, car2y, .05)

    #display with a 60ms refresh rate
    stddraw.show(60)

    #change cars x values randomly to simulate a race
    car1x += random.uniform(0.005, 0.02)
    car2x += random.uniform(0.005, 0.02)

    #break the loop if a car wins so the winner can be displayed
    if car1x >= 1.0 or car2x >= 1.0:
        break

stddraw.clear()

#check who won the race
if car1x > car2x:
    text = "Red Car Wins!"
elif car1x < car2x:
    text = "Blue Car Wins!"
elif car1x == car2x:
    text = "It's a Tie!"

#final screen with the winner displayed
stddraw.setPenColor(stddraw.BLACK)
stddraw.filledSquare(0.0, 1.0, 5)
stddraw.setPenColor(stddraw.WHITE)
stddraw.setFontFamily("Arial")
stddraw.setFontSize(18)
stddraw.text(0.5, 0.5, text)
stddraw.show()


