import turtle
import random


class Shape:
    color = None
    pos = [0, 0]

    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def draw(self):
        turtle.penup()
        turtle.setpos(self.pos[0], self.pos[1])
        turtle.pendown()
        turtle.pencolor(self.color)


    def setColor(self, color):
        self.color = color


class Rectangle(Shape):
    def draw(self, a, b):
        Shape.draw(self)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)


class Triangle(Shape):
    def draw(self, a):
        Shape.draw(self)
        turtle.left(60)
        turtle.forward(a)
        turtle.right(120)
        turtle.forward(a)
        turtle.right(120)
        turtle.forward(a)


class Circle(Shape):
    def draw(self, r):
        Shape.draw(self)
        turtle.circle(r)


c = Circle()
c.setPos(random.randint(-150, 150), random.randint(-150, 150))
c.setColor("black")
c.draw(random.randint(10, 80))

r = Rectangle()
r.setPos(random.randint(-150, 150), random.randint(-150, 150))
r.setColor("red")
r.draw(random.randint(10, 80), random.randint(10, 80))

t = Triangle()
t.setPos(random.randint(-150, 150), random.randint(-150, 150))
t.setColor("blue")
t.draw(random.randint(10, 80))


turtle.exitonclick()
