#MonChefDoeuvre1171.py
#
#Description: An arts project created in Python
#
#Made by: John Chan
#
#Date: March 2017

import turtle as stylus
import math as calc
import random as ran

#Helper Functions
def move_pen(xcoord=0, ycoord=0):
    """
     - Moves the turtle at specified coordinates without drawing anything.
     - Default coordinates is (0,0)
     - Parameters: x coordinate, y coordinate
    """
    stylus.hideturtle()
    stylus.penup()
    stylus.setpos(xcoord, ycoord)
    stylus.pendown()
    stylus.showturtle()
    return 

def set_angle(default=0):
    """
     - Sets angle counter-clockwise to the specified value.
     - Default angle is 0.
     - Parameters: (angle) in degrees
    """
    stylus.hideturtle()
    angle = default-stylus.heading()
    stylus.left(angle)
    stylus.showturtle()
    return

def manage_stylus(color="black", size=1, fill=False, paint="white"):
    """
    -Controls the color palette. No arguments sets parameters to default.
    -Parameters: (color), (size), (fill), (paint)
    -Return: None
    """
    stylus.pencolor(color)
    stylus.pensize(size)
    if(fill==True):
        stylus.fillcolor(paint)
        stylus.begin_fill()
    else:
        stylus.end_fill()
        fillcolor=None
    return

#Art Functions

def draw_parallelogram(height, width, angle=90, skew=90):
    """
     - Draws a general parallelogram. Draws clockwise.
     - Default angle and skew is both 90
     - Angle and Skew is the reference angle. Example, skew = 80  skews 10 from 90
     - Parameters: (angle), (skew), in degrees, (height), (width), of the shape
    """
    turn = angle-90+skew
    for sides in range(4):
        if(sides%2==0):
            set_angle(turn)
            stylus.forward(height)
            turn = turn + (180-skew)
        else:
            set_angle(turn)
            stylus.forward(width)
            turn = turn+skew
    return        

def draw_triangle(len1, len2, angle1=90, rotate=0):
    """
     - Draws a general triangle.
     - Default is a right triangle. No ratation by default
     - Parameters: (base), (side), (angle) in degrees, (rotation) in degrees
    """
    #did not use a loop due to lack of symmetry
    posx = [stylus.xcor()]
    posy = [stylus.ycor()]
    hypo = 0
    angle1rad = (angle1*calc.pi)/180
    set_angle(rotate)
    stylus.forward(len1)
    set_angle(90+(90-angle1)+ rotate)
    stylus.forward(len2)
    posx.append(stylus.xcor())
    posy.append(stylus.ycor())
    hypo = calc.hypot(posx[1]-posx[0], posy[1]-posy[0])
    angle2rad =  calc.acos(((hypo)**2 + (len2)**2 - (len1)**2)/(2*len2*hypo))
    angle2 = calc.degrees(angle2rad)
    set_angle(360-angle1-angle2+rotate)
    stylus.forward(hypo)
    return

def draw_circle(radius, rotation, angle=0):
    """
    -Math to draw a circle. Semicircles are sealed. Default angle to tilt is 0.
    -Parameters: radius, rotation, angle
    """
    distance = 0
    
    set_angle(angle)
    posx = [stylus.xcor()]
    posy = [stylus.ycor()]   
    stylus.circle(radius,rotation)
    if(rotation<360):
        posx.append(stylus.xcor())
        posy.append(stylus.ycor())
        set_angle(0.5*(360-stylus.heading()+angle)+stylus.heading())
        distance = calc.hypot(posx[1]-posx[0],posy[1]-posy[0])
        stylus.forward(distance)
    return

def generate_color():
    """
    -Randomly pick one of five colors: Red, Purple, Blue, Green, Yellow
    -Parameters: None
    -Return: color
    """
    spin = ran.randint(1,5)
    if(spin==1):
        color = "#99ff99"
    elif(spin==2):
        color = "#e600e6"
    elif(spin==3):
        color = "#ffff00"
    elif(spin==4):
        color="#66ffff"
    elif(spin==5):
        color = "#ff6666"
    return color


def draw_star():
    """
    -Draws randomly colored stars. Uses the function generate_color()
    -Parameters: None
    """
    angle = 70 
    step = 5
    size=1
    paint=generate_color()

    manage_stylus("white",size,True,paint)
    for length in range(8):
        if(length%2==0):
            set_angle(angle)
            stylus.forward(step)
            angle=angle-50
        else:
            set_angle(angle)
            stylus.forward(step)
            angle=angle+140
    manage_stylus()
    return

def draw_tree():
    """
    -Computers the shape of a tree.
    -Parameters: None
    """

    x = stylus.xcor()    
    manage_stylus("black",1,True,"#4d1a00")
    draw_parallelogram(20, 10)
    manage_stylus()

    for tiers in range(3):
        manage_stylus("black",1,True,"#264d00")
        move_pen(x-20, stylus.ycor()+20+(tiers-1)*5)
        draw_triangle(30, 70, 77.62637)
        manage_stylus()      
    return

    
#Gallery

def draw_frame():
    """
    -Draws the frame for the entire picture.
    -Parameters: None
    """
    x_coord=[310, 295, 290]
    y_coord=[-310, -295, -290]
    frame=[625, 595, 585]
    boldness = [3,1,1]
    color=["#993300","gold","#333399"]

    for square in range(3):
        move_pen(x_coord[square], y_coord[square])
        manage_stylus("black",boldness[square],True,color[square])
        draw_parallelogram(frame[square],frame[square])
        manage_stylus()
    return

def constellation():
    """
    -Computes the randomly generated constellation. Rejects overlaps.
    -Parameters: None
    """
    stylus.speed(10)
    stars = 30
    coordx=[]
    coordy=[]
    check=0
    invalid = 1
    regen=False
    
    for star in range(stars):
        coordx.append(ran.randint(-285,280))
        coordy.append(ran.randint(80,225))#120-250
        while(invalid-1 < star):
            if(((coordx[invalid-1]+10)>coordx[star] and (coordx[invalid-1]-10)<coordx[star]) and star!=0):
                check=invalid-1
                regen=True
            while(regen):
                coordx[star]=ran.randint(-285,280)
                if((coordx[check]+10)<coordx[star] or (coordx[check]-10)>coordx[star]):                  
                    regen=False
                    invalid=0                    
            invalid=invalid+1
        invalid=1

        move_pen(coordx[star], coordy[star])
        draw_star()
    return

def draw_lake():
    """
    -Draws the lake using a semi-circle
    -Parameters: None
    """
    move_pen(290,-290)
    manage_stylus("black",1,True,"#003333")
    draw_parallelogram(300,585)
    manage_stylus()
    move_pen(-215, 10)
    manage_stylus("black",1,True,"#000066")
    draw_circle(210, 180, -90)
    manage_stylus()
    return

def draw_dock():
    """
    - Draws a dock by the lake using pieces to create board effects
    - Parameters: None
    """
    for stripes in range(10):
        manage_stylus("black",2,True,"#331a00")
        move_pen(-190+(stripes-1)*10, -35)
        draw_parallelogram(30, 13, 90, 95)
        manage_stylus()
    return

def organize_trees():
    """
    -Organizes and builds trees in order using pre-determined coordinates
    -Parameters: None
    """
    x=[215,265,205,240,210,260,275,230,160,120]
    y=[0,-35,-60,-120,-155,-160,-225,-230,-190,-250]
    for tree in range(10):
        move_pen(x[tree],y[tree])
        draw_tree()   
    return

def draw_cabin():
    move_pen(-145,-250)
    #builds the front side of cabin
    for logs in range(10):
        manage_stylus("black",1, True, "#4d1919")
        draw_parallelogram(6, 120)
        manage_stylus()
        move_pen(-145,-250+logs*6)
    #builds the door
    move_pen(-165,-250)
    manage_stylus("black",1, True, "#4d2600")
    draw_parallelogram(32, 15)
    manage_stylus()
    #builds the doorknob
    move_pen(-168,-238)
    manage_stylus("black",1, True, "black")
    draw_circle(2,360)
    manage_stylus()
    #builds the window
    move_pen(-220,-235)
    manage_stylus("black",1,True,"#331a00")
    draw_parallelogram(15,15)
    manage_stylus()
    move_pen(-222,-233)
    manage_stylus("black",1,True,"yellow")
    draw_parallelogram(11,11)
    manage_stylus()
    #builds the roof
    move_pen(-145,-195)
    manage_stylus("black",1,True,"#1a0d00")
    draw_parallelogram(30,120,90,75)
    manage_stylus()
    #builds the triangular roof
    move_pen(-144,-194.5)
    manage_stylus("black",1,True,"#1a0d00")
    draw_triangle(25.357,30,65,10)
    manage_stylus()
    #builds the side bit of the wall
    move_pen(-120,-240)
    for bars in range(9):
        move_pen(-120,-239+(bars)*6)
        manage_stylus("black",1,True, "#4d1919")
        draw_parallelogram(25,6,180,102)
        manage_stylus()
    return
   
#Main Part of Program


draw_frame()
constellation()
draw_lake()
draw_dock()
organize_trees()
draw_cabin()

stylus.hideturtle()
stylus.mainloop()
