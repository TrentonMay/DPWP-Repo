class CarData(object):
    def __init__(self):
        self.person = ""
        self.email = ""
        self.miles = ""
        self.passenger = ""

    @property
    def passenger(self):
        pass
    @passenger.setter
    def passenger(self, x):
        if x > 8:
            print "There is no production vehicle that holds this many people"
        else:
            self.passenger = x

class CalcMPG(object):
    def __init__(self):
        self.miles = ""
        self.gal = ""

    def mpg(self, miles, gal):
        num_miles = int(miles)
        num_gal = int(gal)

        final_mpg = num_miles / num_gal
        print final_mpg


