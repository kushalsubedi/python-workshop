class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print(f"person name is {self.name} and he is {self.age} years old")


p1=person("kushal",21)
p1.show_person()