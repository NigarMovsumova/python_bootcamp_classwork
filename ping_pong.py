import turtle
import os


#ede bilmediklerim:
#border divar elave etmek yeni ki top deyende oyun dayansin
#hereketler

interface = turtle.Screen()
interface.title("The Ping Pong Game")
interface.bgcolor("light blue")
interface.setup(width=1000, height=600)
interface.tracer(0) #hesabin gosterilmesi

# Hesabin ekranda gosterilmesi

score_player1 = 0 #birinci gamer
score_player2 = 0 #ikinci gamer

#  Sol #penup=xetleri ekran uzerinde cizgi buraxmamasini yaradir
pad_left = turtle.Turtle()
pad_left.speed(0)
pad_left.shape("square") #paddlein formasi
pad_left.color("white") #paddlein rengi
pad_left.shapesize(stretch_wid=5, stretch_len=1)
pad_left.penup()
pad_left.goto(-350, 0)

#  Sag
pad_right = turtle.Turtle()
pad_right.speed(0)
pad_right.shape("square")
pad_right.color("white")
pad_right.shapesize(stretch_wid=5, stretch_len=1)
pad_right.penup()
pad_right.goto(350, 0)

# Topun yaradilmasi
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle") #formasi topun
ball.color("white") #rengi
ball.penup()
# ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# hesab
pen = turtle.Turtle()
# pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 20, "normal"))


# Oyunun funksiyalarinin yaradilmasi
def paddle_a_up():
    y = pad_left.ycor()
    y += 20
    pad_left.sety(y)


def paddle_a_down():
    y = pad_left.ycor()
    y -= 20
    pad_left.sety(y)


def paddle_b_up():
    y = pad_right.ycor()
    y += 20
    pad_right.sety(y)


def paddle_b_down():
    y = pad_right.ycor()
    y -= 20
    pad_right.sety(y)


# Her iki oyuncunun paddlelarinin herketi
interface.listen()
interface.onkeypress(paddle_a_up, "w")
interface.onkeypress(paddle_a_down, "s")
interface.onkeypress(paddle_b_up, "Up")
interface.onkeypress(paddle_b_down, "Down")

# while olan hisse
while True:
    interface.update()

    # Topu herekete getirmek
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border ???????(ede bilmedim)

    # yuxari ve asagi
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("")

    # sol ve sag hereketler
    if ball.xcor() > 350:
        score_player1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_player1, score_player2), align="center", font=("Courier", 24, "normal"))
        # ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_player2 = score_player2 + 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(pad_right, score_player2), align="center",
                  font=("Courier", 24, "normal"))
        # ball.goto(0, 0)
        ball.dx *= -1

    # Padin ve topun bir birine deymesi
    if ball.xcor() < -340 and ball.ycor() < pad_right.ycor() + 50 and ball.ycor() > pad_right.ycor() - 50:
        ball.dx *= -1
        os.system("")

    elif ball.xcor() > 340 and ball.ycor() < pad_left.ycor() + 50 and ball.ycor() > pad_left.ycor() - 50:
        ball.dx *= -1
        os.system("")

