import turtle
import winsound         #module for sound effect


#the window
window = turtle.Screen()        #the screen itself
window.title("Pong by Panda")
window.bgpic("tenor.gif")       #background image of the game
window.setup(width=800, height=600)
window.tracer(0)        #stops window from updating until you manually do, it speeds up games


#first paddle
paddle_one = turtle.Turtle()    #turtle object
paddle_one.speed(0)         #making animations smooth, setting speed to max
paddle_one.shape("square")   #shape of paddle
paddle_one.color("white")   #color of paddle
paddle_one.shapesize(stretch_wid=5, stretch_len=1)   #by default the size is 2px*2px
paddle_one.penup()      #normally upon movement turtles draw lines, so in order to remove those use penup(like msw logo)
paddle_one.goto(-350, 0)   #positioning the paddle -350 to x axis and 0 y(vertical align)


#second paddle
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)   #by default the size is 2px*2px, stretching it by 5X and 1X so 20px*1px
paddle_two.penup()
paddle_two.goto(350, 0)   #positioning the paddle 350 to x axis and 0 y(vertical align)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)   #positionng ball at the center
ball.dx = 2             #movement of ball each time (.5px x and .5px y)   #move right
ball.dy = 2         #move up            #only  up and right cuz both are +ve


#score
score_a = 0
score_b = 0


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B:0", align="center", font=("Courier", 20, "normal"))
#print the scoreboard onto the screen


#function
def paddle_one_up():          #move paddle one up with keyboard
    y = paddle_one.ycor()       #assigns initial y coordinate of paddle
    y += 20 #y increases when you go up, y increases by 20px in this case
    paddle_one.sety(y)              #updating y coordinate upon upward movement


def paddle_one_down():          #move paddle one down with keyboard
    y = paddle_one.ycor()       #assigns initial y coordinate of paddle
    y -= 20 #y decreases when you go down, y decreases by 20px in this case
    paddle_one.sety(y)              #updating y coordinate upon downward movement


def paddle_two_up():        #move paddle two up with keyboard
    y = paddle_two.ycor()       #assigns initial y coordinate of paddle
    y += 20 #y increases when you go up, y increases by 20px in this case
    paddle_two.sety(y)              #updating y coordinate upon upward movement


def paddle_two_down():          #move paddle two down with keyboard
    y = paddle_two.ycor()       #assigns initial y coordinate of paddle
    y -= 20 #y decreases when you go down, y decreases by 20px in this case
    paddle_two.sety(y)              #updating y coordinate upon downward movement


#keyboard binding for paddle one and paddle two
window.listen()     #listen for keyboard inputs
window.onkeypress(paddle_one_up, "w")       #when user enters w call function paddle_one_up
window.onkeypress(paddle_one_down, "s")
window.onkeypress(paddle_two_up, "Up")          #when user enters the arrow up keyt call function paddle_two_up
window.onkeypress(paddle_two_down, "Down")


#main game
while True:
    window.update()     #updates screen everytime the loop runs
    #move the ball
    ball.setx(ball.xcor() + ball.dx)    #what this does is it increments the value each time its looped     #first loop 2px; second loop 2+2px and so on
    ball.sety(ball.ycor() + ball.dy)    #same thing for y coordinate


    #border checking
    if ball.ycor()>290:     #if ball y is greater than height of window
        ball.sety(290)      #setting value back to 290 to remove problems
        ball.dy *= -1       #this reverses the direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    #bouncing off border sound


    if ball.ycor()<-290:        #for bottom
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    #bouncing off border sound


    if ball.xcor()>390:     #for right
        ball.goto(0, 0)
        ball.dx *= -1
        score_a +=1
        pen.clear()         #this resets the score each time otherwise it'll get printed on top of each other
        winsound.PlaySound("chime.wav", winsound.SND_ASYNC)
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 20, "normal"))


    if ball.xcor()<-390:     #for left
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        winsound.PlaySound("chime.wav", winsound.SND_ASYNC)
        pen.write(f"Player A: {score_a} | Player B: {score_b}", align="center", font=("Courier", 20, "normal"))


    #paddle-ball collisions
    #ball is within the width of the paddle, 350 is position of paddle and paddle is 10px wide so 340 , less than 350 cuz otherwise it'd bounce off the back of the paddle as well
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()<paddle_two.ycor()+40 and ball.ycor()>paddle_two.ycor()-40):#within height of paddle
        ball.setx(340)      #this sets the value to the value it has on the surface of the paddle
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    #bouncing off paddle sound


    if (ball.xcor()<-340 and ball.xcor()>-350 ) and (ball.ycor()<paddle_one.ycor()+40 and ball.ycor()>paddle_one.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1     #for the left side
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    #bouncing off paddle sound

