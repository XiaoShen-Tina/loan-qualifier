import turtle as Tina
Tina.setup(640, 480)

# Drawing a rectangle
Tina.forward(100)
Tina.right(90)
Tina.forward(50)
Tina.right(90)
Tina.forward(100)
Tina.right(90)
Tina.forward(50)
Tina.reset()

# Box with pause 
Tina.forward(20)
Tina.penup()
Tina.forward(10)
Tina.pendown()
Tina.forward(10)
Tina.pendown()
Tina.forward(20)
Tina.right(90)
Tina.forward(20)
Tina.penup()
Tina.forward(10)
Tina.pendown()
Tina.forward(20)
Tina.penup()
Tina.forward(10)
Tina.pendown()
Tina.forward(20)
Tina.reset()

# Drawing circles
Tina.circle(50)
Tina.forward(10)
Tina.pencolor("red")
Tina.circle(60)
Tina.forward(10)
Tina.pencolor("blue")
Tina.width(5)
Tina.circle(70)
Tina.forward(10)
Tina.pencolor("green")
Tina.width(7)
Tina.fillcolor("purple")
Tina.begin_fill()
Tina.circle(80)
Tina.end_fill()
Tina.reset()

# Drawing circles with goto function
Tina.circle(30)
Tina.penup()
Tina.goto(130,130)
Tina.pendown
Tina.circle(20)
Tina.reset()

# Drawing Olympic flag. color of the circles are blue yellow black green red
# blue
Tina.pencolor("blue")
Tina.circle(50)

# black
Tina.penup()
Tina.goto(120, 0)
Tina.pendown()
Tina.pencolor("black")
Tina.circle(50)

# red
Tina.penup()
Tina.goto(240, 0)
Tina.pendown()
Tina.pencolor("red")
Tina.circle(50)

# yellow
Tina.penup()
Tina.goto(60, -50)
Tina.pendown()
Tina.pencolor("yellow")
Tina.circle(50)

# green
Tina.penup()
Tina.goto(180, -50)
Tina.pendown()
Tina.pencolor("green")
Tina.circle(50)
Tina.hideturtle()
Tina.done()




