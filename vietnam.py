from turtle import*
hideturtle()
pensize(5)
speed(-50)
b=3
bgcolor("black")
x,y=position()
penup()
backward(25)
left(90)
forward(150)
right(90)
backward(200)
speed(b)
begin_fill()
color("red")
pendown()
forward(500)
right(90)
forward(360)
right(90)
forward(500)
right(90)
forward(360)
end_fill()
penup()
speed()
goto(x,y)
pendown()
begin_fill()
color('yellow')
right(90)
left(72)
speed(b)
a=80
for i in range(4):
    forward(a)
    right(144)
    forward(a)
    left(72)
forward(a)
right(144)
forward(a)
end_fill()
speed()
penup()
left(90)
backward(250)
done()
