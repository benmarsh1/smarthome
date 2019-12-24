
class Items:
    class Light:
        def colour(self,r,g,b):
            self.r=r
            self.g=g
            self.b=b
    def __init__(self,name):
        self.name=name

    def onoff(self,state):
        self.state=state

    def querystate(self):
        print("{} is {} right now.".format(self.name.capitalize(), self.state))


