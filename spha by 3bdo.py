import turtle


# create a window

window = turtle.Screen()

window.bgcolor('gray4')

window.title('Bearish by 3bdo')

window.setup(600, 600)


# create a counter
jls_extract_var = "التسبيحات"

count = 0
num_turtle = turtle.Turtle()

num_turtle.penup()

num_turtle.hideturtle()

num_turtle.color('#3c79b8')

num_turtle.goto(0, 150)

num_turtle.write(str(count), align='center', font=('Arefraqua', 50))


# create a button

button = turtle.Turtle()

button.color('#3c79b8')

button.shape('circle')

button.shapesize(10, 10)


# increment the count and update the display

def click_button(x, y):

    global count

    count += 1
    num_turtle.clear()

    num_turtle.write(str(count), align='center', font=('Arefraqua', 50))

turtle.listen()

turtle.onscreenclick(click_button)

turtle.mainloop()

