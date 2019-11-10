# Simple Pong game In Python
# for learning Python

import turtle 
#turtle is a simple module used for # #basic graphics, for beginners


wn = turtle.Screen()
#creating a window 
wn.title("Ping Pong")
#giving a title to the window
wn.bgcolor("black")
#changing the background color to black
wn.setup(width=800,height=600)
#setting up the size of the window
wn.tracer(delay=0)
#tracer stops the window from updating and
#we have to manually update it, what this
#let's us do is speed up our game without this our games would run much slower


#Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
#creating a turtle obj of paddle_a name where turtle is the module and Turtle is the class
paddle_a.speed(0)
#this sets the speed of the animation,this is something that has to be done for the turtle module, what this does is that it sets the speed of it to the maximum possible speed , otherwise things will be really slow
paddle_a.shape("square")
#here we are giving the paddle a shape,square is a built in shape
paddle_a.color("white")
#here we are giving the paddle a color
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#the paddle as seen in the game is long but the default value of the paddle is just 20 by 20 pixels hence we stretch it using shapesize method, we stretch width by 5 times and leave len as it is so that the paddle becomes longer(100px)
paddle_a.penup()
#turtle by definition draw a line as they are moving, penup() method is used to stop that
paddle_a.goto(-350,0)
#giving initial position to paddle at left side middle,at start coordinate(-350,0), The center of the window is (0,0)


# Paddle B
#doing the same as paddle a
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
#for ball we do the same as paddle but we do not stretch it and we position it at center
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3
#dx where d means delta or change, hence change in x coordinate, similarly with dy, we assign them appropriate value to smoothen the movement. what this means is that everytime our ball moves it moves by 2 px , since x is positive its going to move right , and y is positive hence it's going to move up , hence it will move diagonally


#FOR SCORINg
#Pen(using it for scoring mechanism)
pen = turtle.Turtle()
pen.speed(0)
#we make a turtle object of pen set the animation speed
pen.color("white")
#color set as white
pen.penup()
#penup used as we don't want it to draw line
pen.hideturtle()
#we hide as we don't want to see it,we just want to see the text it's going to write
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a,score_b) ,align="center" , font=("Courier",24,"normal"))


#Function to move paddle A up
def paddle_a_up():
  y = paddle_a.ycor()
  #to move the paddle we need to know the current y-coordinate ycor() method returns the current ycoordinate of the object
  y +=20
  #as we need to move up we add 20 px value each time to y as we move up
  paddle_a.sety(y)
  #after calculating the value we pass the value to the object so that it can move


#Function to move paddle A down(same logic as above)
def paddle_a_down():
  y = paddle_a.ycor()
  y-=20
  paddle_a.sety(y)


#function to move paddle B up(same logic as paddle_a_up)
def paddle_b_up():
  y = paddle_b.ycor()
  y+=20
  paddle_b.sety(y)


#function to move paddle B down(same logic as paddle_a_down)
def paddle_b_down():
  y =paddle_b.ycor()
  y-=20
  paddle_b.sety(y)


# Keyboard binding
# to bind the function's to the keys to move to paddle
wn.listen()
#listen tells the window to listen for keyboard inputs
wn.onkeypress(paddle_a_up,"w")
#the onkeypress function binds the paddle_a_up function to "w" key hence whenever w key is pressed paddle a will move up
wn.onkeypress(paddle_a_down,"s")
#binding the paddle_a_down function to "s"
wn.onkeypress(paddle_b_up,"Up")
#binding the paddle_b_up function to "Up"
wn.onkeypress(paddle_b_down,"Down")
#binding the paddle_b_down function to "Down"


#Main game loop
while True:
  wn.update()
  #what update does is that everytime loop runs it updates the screen
  
  #Move the ball
  ball.setx(ball.xcor() + ball.dx)
  #adding the change in x coordinate to the present x coordinate
  ball.sety(ball.ycor() + ball.dy)
  #adding the change in y to present y coordinate, hence from above and this change the ball will move


  #Border checking
  # we perform border checking to restrict the ball's movement inside the window
  #Top border
  if ball.ycor() > 290:
    # here we compare the current y coordinate of the ball to the upper limit of the y coordinate(300,-300) but here we use 290 for safety
    ball.sety(290)
    # we are setting the ball's coordinate here to 290 for safety
    ball.dy *=-1
    # what this does is that it reverses the direction of the ball by changing the dy from positive to negative, hence the ball starts moving towards the negative direction


  #Bottom border(same logic as Top border)
  if  ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    #here we do the same as Top logic, because the dy as it is moving downwards must be negative, hence to make it move upwards we have to multiply it with a negative number to turn it positive.
  

  #Right Side border(condition when Player A wins a point)
  if ball.xcor() > 390:
    #we compare the current value of the x coordinate of the ball object to the maximum range of x(400,-400) but we use 390 for safety
    ball.goto(0,0)
    # As we are checking side borders for win conditions, hence when the ball has already went past the border, it means one point is over and it will go back to starting pos(0,0)
    ball.dx *=-1
    #we are changing the direction of the ball after each point
    score_a +=1
    #increasing player A's score by 1
    pen.clear()
    #clearing the screen
    pen.write("Player A: {} Player B: {}".format(score_a,score_b) ,align="center" , font=("Courier",24,"normal"))
    #updating the score


  #Left Side border(same logic as right)(when Player B wins a point)
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *=-1
    #changing the polarity of dx each time to move the ball in different direction after each play
    score_b +=1
    #increasing the score of player B by 1
    pen.clear()
    #here we are clearing the score because otherwise updation will happen on top of it
    pen.write("Player A: {} Player B: {}".format(score_a,score_b) ,align="center" , font=("Courier",24,"normal"))
    #updating the score


  # Paddle and Ball collisions
  #Collision with Paddle B condition
  if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
    #here we are basically checking the condition when ball falls on paddle B, it can only happen when the ball is more than 340 and less is than 350 on xaxis(which is the paddle b's x coordinate) and stays in between the range of the paddle B i.e. the paddle B's (y coordinate +/- 40) (we should take 50 for the range of the paddle but we have to compensate for the size of the ball which is 20px, we can draw it on paper and understand), as the paddle.ycor() returns only the value of y coordinate of it's center to cover the whole paddle B(i.e 100px in size) we set the lower range at (paddle_b.ycor()-50) and the upper range at (paddle_b.ycor()+50) .
    ball.setx(340)
    #we basically move the ball back to 340,because once the ball falls into this range we dont want it to keep moving and just change direction at that point.
    ball.dx *=-1
    #we multiply the value of ball.dx with -1 to change it polarity hence it's direction, Which means when the ball will collide it will start moving in the other direction

  #Collision with Paddle A condition(same logic as paddle b)
  if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
    ball.setx(-340)
    ball.dx *=-1
    #the only change here is that paddle A lies in the left side hence the negative values for xcoordinates




  