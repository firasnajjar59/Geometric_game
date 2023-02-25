class Rectangle:
    def __init__(self,first_point,second_point):
        self.first_point=first_point
        self.second_point=second_point
        self.width=self.second_point.x-self.first_point.x
        self.length=self.second_point.y-self.first_point.y
    def __str__(self):
        return f"Lower point: {self.first_point}, Upper point: {self.second_point}."
    def area_offset(self,area_to_compare):
        return self.width*self.length-area_to_compare
    def area(self):
        return self.width*self.length
    def draw_rectanglr(self,canvas):
        canvas.penup()
        canvas.goto(self.first_point.x,self.first_point.y)
        canvas.pendown()
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.length)
        canvas.left(90)
        canvas.forward(self.width)
        canvas.left(90)
        canvas.forward(self.length)
        canvas.left(90)