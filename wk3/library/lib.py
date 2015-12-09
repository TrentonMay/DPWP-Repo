class CarData(object):
    def __init__(self):
        self.__passenger = ""
        self.__type = ""
        self.__alt_type = ""

    @property
    def passenger(self):
        return self.__passenger
    @passenger.setter
    def passenger(self, x):
        if int(x) > 8:
            print "There is no production vehicle that holds this many people"
        else:
            self.__passenger = x
    def car_type(self, passenger):
        passenger = self.__passenger
        if passenger == 1:
            self.__type = "Muscle"
            self.__alt_type = "Sport"
            return self.__type + " " + self.__alt_type
        elif passenger < 8 and passenger > 4:
            self.__type = "Van"
            self.__alt_type = "SUV"
            return self.__type + " " + self.__alt_type
        elif passenger > 1 and passenger < 4:
            self.__type = "Sedan"
            self.__alt_type = "4-Seat Coup"
            return self.__type + " " + self.__alt_type
        else:
            self.__type = "We couldn't find a vehicle for you"
            self.__alt_type = "We couldn't find a alternate car for you"
            print "There is no car that fits your needs"
            return self.__type + " and " + self.__alt_type


class CalcMPG(object):
    def __init__(self):
        self.__miles = ""
        self.__gal = ""

    def mpg(self, miles, gal):
        num_miles = int(miles)
        num_gal = int(gal)

        final_mpg = num_miles / num_gal
        print "Your mpg is " + str(final_mpg) + " miles per gallon"
        return final_mpg

class FinalCar(object):
    def __init__(self):
        pass



