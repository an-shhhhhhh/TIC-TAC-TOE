# in this exercise we will see the class variable and it's uses
class Circle:
    pi=3.14

    @classmethod
    def names(cls): #class method-----> This method by default calls the class.
        return print(f"Hey there this {cls.__name__} class is printing the area the of the circle and and dont't forget about the circumference")

    @staticmethod
    def mee():
        return print(f"Hey guys, WELCOME to the function of {cls.__name__} class that prints the area and circumference of the circle when you enter the value of the radius. And guess what ? You are now inside the STATIC METHOD or I may say that you have been called by the static method")

    def __init__(self,radius): #instance method ---->this method by default directly calls the object / instance.
        self.radius=radius
    def circumference(self):
        circumference=2*Circle.pi*self.radius
        return circumference
    def area(self):
        area=Circle.pi*self.radius*self.radius
        return area

c1=Circle(4)
print(c1.circumference())
print(c1.area())
print(Circle.names())
print(Circle.mee(cls))