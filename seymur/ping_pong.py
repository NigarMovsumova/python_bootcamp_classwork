import turtle
import winsound

# 0. Suret meselesine baxmaq
# 1. Istifadechi adlarini sorushmaq
# 2. Suret yaratmasi - ?
# 3. Neche xala kimi oynanilir sorushmaq

# Oyuncularin hesabi (score)
import winsound
score_player1 = 0  # birinci oyuncu soldaki
score_player2 = 0  # ikinci oyuncu sagdaki
# Interface"in yaradilmasi
# penup her hansisa bir obyektin hereketi zamani trayektoriyasinin izini ekranda saxlamamasidir
interface = turtle.Screen()
interface.title("Ping Pong Game")  # Oyunun adi
interface.bgcolor("black")  # backgroundun rengi
interface.setup(height=600, width=800)  # ekran olculeri
interface.tracer(0)
# Paddle 1 yaradilmasi
pad_1 = turtle.Turtle()
pad_1.speed(0)  # padin sureti
pad_1.color("white")  # padin remgi
pad_1.shape("square")  # padin formasi
pad_1.shapesize(stretch_wid=5, stretch_len=1)  # padin sahesi eni uzunlugu
pad_1.penup()
pad_1.goto(-350, 0)
# Paddle 2
pad_2 = turtle.Turtle()
pad_2.speed(1)
pad_2.shape("square")
pad_2.color("white")
pad_2.shapesize(stretch_wid=5, stretch_len=1)
pad_2.penup()
pad_2.goto(350, 0)
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Calibri", 24, "normal"))
# Top
ball = turtle.Turtle()
ball.speed(0.5)  # topun sureti
ball.shape("circle")  # topun formasi
ball.color("white")  # topun rengi
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1.5

# Funksiyalar
def pad_1_up():
    y = pad_1.ycor()
    y = y + 15
    pad_1.sety(y)

def pad_1_down():
    y = pad_1.ycor()
    y = y - 15
    pad_1.sety(y)

def pad_2_up():
    y = pad_2.ycor()
    y = y + 15
    pad_2.sety(y)

def pad_2_down():
    y = pad_2.ycor()
    y = y - 15
    pad_2.sety(y)
def start_game():
    pass

# Klaviatura idareetmesi
interface.listen()
interface.onkey(pad_1_up, "w")
interface.onkey(pad_1_down, "s")
interface.onkey(pad_2_up, "Up")
interface.onkey(pad_2_down, "Down")
#interface.onkey(start_game,"Enter")
# Looplar
while True:
    interface.update()
    # Topun hereketi
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Borderleri?
    # yuxari ve asagi
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
        os.system("afplay wallhit.wav&")
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
        os.system("afplay wallhit.wav&")
    # Left and right
    if ball.xcor() > 350:
        score_player1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_player1, score_player2),
                  align="center",
                  font=("Calibri", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -390:
        score_player2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_player1, score_player2),
                  align="center",
                  font=("Calibri", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    # Pad ile topun temasi
    if ball.xcor() < -340 and ball.ycor() < pad_1.ycor() + 40 and ball.ycor() > pad_1.ycor() - 40:
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.xcor() > 340 and ball.ycor() < pad_2.ycor() + 40 and ball.ycor() > pad_2.ycor() - 40:
        ball.dx = ball.dx * -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)