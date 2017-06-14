import inspect

class car(object):
    def __init__(self):
        self.wheels=4
        self.engine=True
        self.printwheels()

    def printwheels(self):
        print "no of wheels",self.wheels

class fiesta(car):
    def __init__(self, colour="White", spoiler=False, alloys=False):
        super(fiesta, self).__init__()
        self.colour= colour
        self.spoiler= spoiler
        self.alloys= alloys
class fivewheelfiesta(fiesta):
    def __init__(self):
        super(fivewheelfiesta, self).__init__()
        self.wheels=5
        self.printwheels()
    def printwheels(self):
        print "no of wheels",self.wheels

newfiesta=fivewheelfiesta()
print dir(newfiesta)

