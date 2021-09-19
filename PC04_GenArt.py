"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Jessica Hamilton-Burns

********* HEY, READ THIS FIRST **********

My PC04 is based off of the Spongebob episode, Jellyfish Jam. During this episode, Spongebob brings home a bunch of jellyfish and they stay up all night playing music. 
I immediately thought of this episode after seeing other generative art examples, because it is very colorful and there are frequent background changes. 
Therefore, I created a jellyfish out of half an ellipse, lines, dots, and a spirograph. In addition, I used random to change my jellyfish color and the background of the panel.
I believe this project feels like you are at a party and evokes positive emotions. 

"""
import turtle
import math, random

turtle.colormode(255) # allow for a wide variety of colors

# Create a panel to draw on. 
panel = turtle.Screen()
w = 500 # width of panel based on spongebob gif size
h = 370 # height of panel based on spongebob gif size
panel.setup(width=w, height=h) #based on spongebob gif size

images = ["spongebob_big_dance.gif", "spongebob_big_dance2.gif", "spongebob_big_dance3.gif", "spongebob_big_dance4.gif", "spongebob_big_dance5.gif"] # different spongebob jellyfish backgrounds
image = random.choice(images) # randomly select different backgrounds
panel.bgcolor(0, 71, 171) # add panel background color just in case the background doesn't fill the screen
panel.bgpic(image) # place the random images in the background

jellyB = turtle.Turtle() # change turtle name for jellyfish body
partyColors = [(255, 0, 0), (255, 135, 0), (255, 211, 0), (222, 255, 10), (161, 255, 10), (10, 255, 153), (10, 239, 255), (20, 125, 245), (88, 10, 255), (190, 10, 255)] # different bright party colors
jellyB.color(random.choice(partyColors)) # randomly select different party colors for the body of the jellyfish
jellyB.speed(10) # fast speed 
jellyB.pensize(5) # thick pensize for the body of the jellyfish
jellyB.goto(0,0) # send jellyB to center of the screen 

# modified from Alejandra's parametric pseudocode assignment
radX1 = 7 # defining the x axis
radY1 = 5 # defining the y axis
scale = 10 # defining the scale of the jellyfish body

ANGLES = range(0,181) # select the range to half the ellips
for angle in ANGLES:
    angle = math.radians(angle)      

angle = range(0,181) 
jellyB.begin_fill() # signal to JellyB that we will fill with random colors
for angle in ANGLES:
    angle = math.radians(angle)
    X = scale * math.cos(angle) * radY1 
    Y = scale * math.sin(angle) * radX1
    jellyB.goto(X,Y) # send jellyB to X and Y to create half ellipse/top of jellyfish
jellyB.goto(0,0) # sned jellyB back to center to complete shape
jellyB.end_fill() # signal to JellyB to fill with random color

# legs of jellyfish
jellyB.up() # pickup pen 
jellyB.goto(-50,0) # send jellyB to edge of jellyfish 
jellyB.down() # set down the pen
jellyB.goto(-65,-10) # send jellyB to begin forming the first leg
jellyB.left(5) # adjust jellyB angle
jellyB.goto(-35,-40) # send jellyB to second point of the first leg
jellyB.goto(-95,-70) # send jellyB to final point to finish first leg

# repeat for remaining 4 legs. Adjust placement on the X axis 25 to the right
jellyB.up()
jellyB.goto(-25,0)
jellyB.down()
jellyB.goto(-40,-10)
jellyB.left(5)
jellyB.goto(-10,-40)
jellyB.goto(-70,-70)

jellyB.up()
jellyB.goto(0,0)
jellyB.down()
jellyB.goto(-15,-10)
jellyB.left(5)
jellyB.goto(15,-40)
jellyB.goto(-45,-70)

jellyB.up()
jellyB.goto(25,0)
jellyB.down()
jellyB.goto(10,-10)
jellyB.left(5)
jellyB.goto(40,-40)
jellyB.goto(-20,-70)
   
jellyB.up()
jellyB.goto(50,0)
jellyB.down()
jellyB.goto(35,-10)
jellyB.left(5)
jellyB.goto(65,-40)
jellyB.goto(5,-70) 

# jellyfish spots
spots = turtle.Turtle() # change turtle name for jellyfish spots
spotColors = [(102, 0, 0), (204, 109, 0), (224, 187, 0), (194, 224, 0), (138, 224, 0), (0, 163, 95), (0, 133, 143), (6, 67, 137), (45, 0, 143), (120, 0, 163)] # different spot colors that are different shades of the party colors
spots.color(random.choice(spotColors)) # have colors randomly selected
spots.speed(10) # fastest speed
    
spots.up() # pen up
spots.goto(-10,20) # send spots to different parts of the jellyfish body
spots.down() # set pen down
spots.dot(15) # draw dot

# repeated steps from above. Placing spots randomly on the jellyfish body
spots.up()
spots.goto(10,50)
spots.down()
spots.dot(10)

spots.up()
spots.goto(20,25)
spots.down()
spots.dot(10)

spots.up()
spots.goto(-25,50)
spots.down()
spots.dot(15)

spots.up()
spots.goto(35,15)
spots.down()
spots.dot(20)

# I used this for loop in the PC03 spirograph project, but have modified it for this project
inc = 5 # set the angle of the increment
numIt = int(360/inc) # set the increment
innerCirc = 1 # radius of inner circle
radius = 3 # radius of outer circles

# set spots location 
spots.up()
spots.goto(-40,10)

# use for loop to create spirograph
for iteration in range(numIt):
    spots.down()
    spots.circle(radius)
    spots.forward(innerCirc)
    spots.left(inc)  
spots.up()

panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
turtle.done()
