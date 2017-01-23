class employee:
    name = ""
    age = 0
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def print_employee(self):
        if self.name == "sneha" :
            print self.name+" kamat "+str(self.age)
        elif self.name == "avin" :
            print self.name

class e12(employee):
    pass

e1 = employee("avin",10)
e1.print_employee()
e2 = e12("sneha",22)

e2.print_employee()