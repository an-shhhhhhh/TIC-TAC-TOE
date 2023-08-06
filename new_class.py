# cheers to my first class
# hehuuuuuu
# lets get started
class Person: #We should always start our class name with capital letters, i dont know why but we should!
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

# defining objects/instance----> instance and objects are the same.
# all these p1,p2,p3 are called objects
p1=Person("anshika","kumari",19)
print(p1.first_name)
print(p1.last_name)