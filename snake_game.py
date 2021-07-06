import random
import turtle
import time


# 1. Seviyyeler - 3 seviyyeden , hansi seviyyedir
# 2. Divar - ?
# 3. xal deyishen adi


delay = 0.50
window = turtle.Screen()
window.title('snake gameƏƏƏ')
window.bgcolor('lightblue')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.80, 0.80)
food.goto(0, 0)

queues = []
point = 0

xal = turtle.Turtle()
xal.speed(0)
xal.shape("square")
xal.color("white")
xal.penup()
xal.hideturtle()
xal.goto(0, 260)
xal.write("point: {}".format(point), align="center", font=("Courier", 24, "normal"))


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

while True:
    window.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for queue in queues:
            queue.goto(1000, 1000)
        queues = []

        point = 0
        delay = 0.5

        xal.clear()
        xal.write("point: {}".format(point), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        new_queue = turtle.Turtle()
        new_queue.speed(0)
        new_queue.shape("square")
        new_queue.color("white")
        new_queue.penup()
        queues.append(new_queue)

        delay -= 0.001

        point = point + 10
        xal.clear()
        xal.write("point: {}".format(point), align="center", font=("Courier", 24, "normal"))

    for index in range(len(queues) - 1, 0, -1):
        x = queues[index - 1].xcor()
        y = queues[index - 1].ycor()
        queues[index].goto(x, y)

    if len(queues) > 0:
        x = head.xcor()
        y = head.ycor()
        queues[0].goto(x, y)

    move()

    for segment in queues:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in queues:
                segment.goto(1000, 1000)
            queues = []
            point = 0
            xal.clear()
            xal.write('point: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            spead = 0.15

    time.sleep(delay)
