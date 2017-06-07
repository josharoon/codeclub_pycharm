class car(object):
    def __init__(self):
        self.wheels=4
        self.engine=True
        self.printwheels()

    def printwheels(self):
        print "no of wheels",self.wheels

class fiesta(car):
    def __init__(self):
        super(fiesta, self).__init__()
        self.colour="Red"

instance1=fiesta()
print instance1.colour
