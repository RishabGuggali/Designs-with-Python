import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(5)
turtle.bgcolor("lightblue")

# Define function to draw the approximate shape of Australia
def draw_australia():
    t.penup()
    t.goto(-180, 100)  # Starting point for the map
    t.pendown()
    
    # Outline of Australia (simplified)
    t.begin_fill()
    t.color("orange")  # Color of the landmass
    t.setheading(240)
    t.circle(90, 120)
    t.setheading(270)
    t.forward(100)
    t.setheading(320)
    t.circle(100, 60)
    t.setheading(240)
    t.circle(120, 90)
    t.setheading(0)
    t.forward(180)
    t.setheading(90)
    t.circle(60, 90)
    t.setheading(240)
    t.circle(120, 90)
    t.setheading(180)
    t.forward(100)
    t.setheading(130)
    t.circle(60, 120)
    t.end_fill()

    # Tasmania (small island below)
    t.penup()
    t.goto(-60, -200)
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.circle(40, 360)  # Tasmania as a small circle
    t.end_fill()

# Call the function to draw Australia
draw_australia()

# Hide the turtle after drawing
t.hideturtle()

# Complete drawing
turtle.done()
