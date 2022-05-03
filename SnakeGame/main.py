import random
import turtle #Window Graphic Library
import time
import random


posponer = 0.1                                      #Reducir tiempo de ejecución


###### WINDOW DESIGN

wn = turtle.Screen()                                #Object window creation
wn.title("SnakeGame")                               #Window title
wn.bgcolor("violet")                                #Window background color
wn.setup(width = 600, height = 600)                 #Window size
wn.tracer(0)                                        #Animation upgrader

###### SNAKE DESIGN

head = turtle.Turtle()                            #Objetc snake creation
head.speed(0)                                     #Speed set up
head.shape("square")                              #Shape set up
head.penup()                                      #
head.goto(0, 0)                                   #Main location
head.direction = "stop"                           #Non-direction set up
head.color("black")                               #Color
head.shapesize(1)                                 #Size(Predetermined in this case)


###### FOOD DESIGN

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))
food.color("red")


###### SNAKE TAIL DEFINITION

tail = []



###### END GAME TEXT

text = turtle.Turtle()
text.speed(0)
text.color("black")
text.penup()                    ###Eliminar recorrido
text.hideturtle()               ## esconder objeto
text.goto(0, 260)
text.write("SCORE:0         HIGH SCORE:0", align = "center", font = ("Courier", 24, "normal" ))

##### SCORE COUNTER CREATION

score = 0
high_score = 0

###### FUNCTIONS


### Snake traslation

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "rigth":
        x = head.xcor()
        head.setx(x + 20)


### Snake rotation

def up():
    head.direction = "up"

def down():
    head.direction = "down"

def left():
    head.direction = "left"

def rigth():
    head.direction = "rigth"


### Set Keyboard

wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(rigth, "Right")

while True:
    wn.update()

    # When distance between snake and food is <20, means they are together. So snake eats the food
    if head.distance(food) < 20:

        # Set random new coordinates of food

        # The movement is always 20px and the snake´s and food´s size too. So if the window is 600px x 600px
        # (300px x 300px per quadrant) don't need to count borders(300 - 20 = 280) because we need to lose when snake
        # touch them.

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        ###### SNAKE TAIL DESIGN
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.penup()
        new_tail.color("grey")
        new_tail.shapesize(1)
        tail.append(new_tail)

        ### Increase Score
        score += 10

        ### Set new High Score
        if score > high_score:
            high_score = score

            ### Clean previous text
            text.clear()

            ### Print text
            text.write("SCORE: {}       HIGH SCORE: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal" ))

    ### Snake tail movement

    tail_size = len(tail)
    for i in range(tail_size - 1, 0, -1):
        x = tail[i - 1].xcor ()
        y = tail[i - 1].ycor()
        tail[i].goto(x, y)

    if tail_size > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x, y)

    ### Body colition

    

    ### Border colition

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:

        # Game Pause
        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        # Remove tail from window size(600px x 600px)
        for i in tail:
            i.goto(1000, 1000)

        # Clean tail from window
        tail.clear()

        # Reset score
        score = 0
        text.clear()
        text.write("SCORE: {}       HIGH SCORE: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal" ))

    mov()
    time.sleep(posponer)


