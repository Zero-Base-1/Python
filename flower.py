import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.speed(10)
flower.pencolor("purple")

# Draw a single petal
def draw_petal():
    flower.circle(180, 60)
    flower.left(120)
    flower.circle(180, 60)
    flower.left(120)

# Draw all petals
for _ in range(4):
    draw_petal()
    flower.left(90)

# flower center
flower.penup()
flower.goto(0, -40)
flower.pendown()
flower.begin_fill()
flower.color("yellow")
flower.circle(40)
flower.end_fill()

# Hide turtle and wait for click
flower.hideturtle()
screen.exitonclick()