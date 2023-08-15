import turtle

# Create a turtle object
t = turtle.Turtle()

colors = ["green", "white", "red"]
turtle.bgcolor("black")

for i in range(200):
    t.pencolor(colors[i % 3])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)  # Specify the angle for turning left

# Keep the window open until it's closed by the user
turtle.done()
