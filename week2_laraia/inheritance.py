class pointFormat0(object):
    x=0
    y=0
    z=0

class pointFormat1(pointFormat0):
    gpsTime=0

##############################

class oldObj():
    def __init__(self,data):
        self.data=data

    def function(self):
        print(self.data**2)

class newObj(oldObj):

    def function(self):
        print(self.data**1.5)

###############################


