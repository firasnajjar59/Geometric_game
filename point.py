class Point:
    def __init__(self, name, age):
        self.x = name
        self.y = age
    def __str__(self):
        return f"({self.x},{self.y})"
    def fall_in_rectangle(self,rec):
        if rec.first_point.x<self.x<rec.second_point.x and rec.first_point.y<self.y<rec.second_point.y:
            return True
        else:
            return False
    def draw_point(self,canvas,size=10, color="red"):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.dot(size,color)

