#imports the turtle setup
import turtle

#sets up the center turtle
sammySeaTurtle = turtle.Turtle()

#changes the shape of the turtle
sammySeaTurtle.shape('turtle')

#changes the turtle color to blue
sammySeaTurtle.color('light green')

#stamps turtle at the start
sammySeaTurtle.stamp()

#sets up the color of the window
turtle.bgcolor("teal")

#deletes the line that follows the turtle
sammySeaTurtle.penup()

#sets up the for loop to repeat 12 times like a clock face
for x in range(12):
    sammySeaTurtle.forward(130)
    #sets the extra little trace line for the clock face
    sammySeaTurtle.pendown()
    sammySeaTurtle.forward(30)
    #places a turtle stamp at the end of the line
    sammySeaTurtle.penup()
    sammySeaTurtle.forward(40)
    sammySeaTurtle.stamp()
    #moves the turtle back to the starting point and then turns to start again
    sammySeaTurtle.backward(200)
    sammySeaTurtle.left(360/12)
    
