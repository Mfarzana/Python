class Introduce:
    #constructor
    def __init__(self, name, age):
        self.name=name
        self.age=age
        #function
    def introduce_self(self):
        print(" My name is "+self.name+" and I am  "+self.age+" years old")


intro=Introduce("Farzana","26")
intro.introduce_self();
