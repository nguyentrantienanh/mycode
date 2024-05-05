from turtle import* #import thu vien
hideturtle() # an hinh anh con rua
pensize(5) #kich thuc but ve
speed(0) # toc do ve nhanh
b=3
bgcolor("black")
x,y=position() # luu vi tri con rua vao y ,x
penup() #nhat but
backward(25)# di chuy con rua ve sau 25
left(90)# cho con rau sang trai
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
speed(0)
goto(x,y)
pendown()
begin_fill()# la co do chua co sao
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
speed(0)
penup()
left(90)
backward(250)