class Parent():
    def __init__(self,last_name,eye_color):
        print ("Parent Constructor")
        self.last_name=last_name
        self.eye_color=eye_color

    def show_info(self):
        print (self.last_name)
        print (self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print ("Child constructor")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys=no_of_toys

    def show_info(self):
        print (self.last_name)
        print (self.eye_color)
        print (self.no_of_toys)

billy_cirus= Parent("Cirus","blue")
#print (billy_cirus.last_name)
billy_cirus.show_info()

print ""

miley_cirus=Child("Cirus","blue",5)
#print (miley_cirus.last_name)
#print (miley_cirus.no_of_toys)
miley_cirus.show_info()