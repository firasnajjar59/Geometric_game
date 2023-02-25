from point import Point
from rectangle import Rectangle
from random import randint
import turtle
point1=Point(randint(0,100),randint(0,100))
point2=Point(randint(100,400),randint(100,400))
rec=Rectangle(point1,point2)
print(f"The rectangle points: {rec}")
print("Guess point that fall in the rectangle: ")
user_point=Point(int(input("Guess x coor: ")),int(input("Guess y coor: ")))
user_area=input("Guess rectangle area: ")
print(user_point.fall_in_rectangle(rec))
print(rec.area_offset(int(user_area)))
screen=turtle.Screen()
screen.setup(900,900)
my_turtle=turtle.Turtle()
user_point.draw_point(my_turtle)
rec.draw_rectanglr(my_turtle)
turtle.done()