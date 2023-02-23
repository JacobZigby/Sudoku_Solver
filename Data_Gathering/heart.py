import turtle

# create a turtle object
heart = turtle.Turtle()

# set the color and width of the line
heart.color('red')
heart.width(2)

# move the turtle to the starting point of the heart shape
heart.penup()
heart.goto(0, -150)
heart.pendown()

# draw the heart shape
heart.begin_fill()
heart.left(45)
heart.forward(200)
heart.circle(100, 180)
heart.right(90)
heart.circle(100, 180)
heart.forward(200)
heart.end_fill()

# hide the turtle
heart.hideturtle()

heart.color('blue')
heart.width(2)

# move the turtle to the starting point of the heart shape
heart.penup()
heart.goto(0, -125)
heart.pendown()

# draw the heart shape
heart.begin_fill()
heart.left(45)
heart.forward(150)
heart.circle(50, 180)
heart.right(90)
heart.circle(50, 180)
heart.forward(150)
heart.end_fill()

# hide the turtle
heart.hideturtle()

# keep the window open
turtle.done()
