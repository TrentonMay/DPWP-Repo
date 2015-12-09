class CarData(object):
    def __init__(self):
        self.__passenger = ""

    @property
    def passenger(self):
        return self.__passenger
    @passenger.setter
    def passenger(self, x):
        if int(x) > 8:
            print "There is no production vehicle that holds this many people"
        else:
            self.__passenger = x


class CalcMPG(object):
    def __init__(self):
        self.__miles = ""
        self.__gal = ""
        self.__final_mpg = 0

    def mpg(self, miles, gal):
        num_miles = int(miles)
        num_gal = int(gal)

        final_mpg = num_miles / num_gal
        print "Your mpg is " + str(final_mpg) + " miles per gallon"
        self.__final_mpg = final_mpg
        return final_mpg

class FinalCar(object):
    def __init__(self):
        self.__type = ""
        self.__alt_type = ""
        self.__type2 = ""
        self.__alt_type2 = ""



    def car_from_passengers(self, people):
        x = people
        if x == 1:
            self.__type = "Muscle"
            self.__alt_type = "Sport"
            return self.__type + " " + self.__alt_type
        elif x < 8 and x > 4:
            self.__type = "Van"
            self.__alt_type = "SUV"
            return self.__type + " " + self.__alt_type
        elif x > 1 and x < 4:
            self.__type = "Sedan"
            self.__alt_type = "4-Seat Coup"
            return self.__type + " " + self.__alt_type
        else:
            self.__type = "We couldn't find a car for you based on passengers"
            self.__alt_type = "We couldn't find an alternate car for you based on passengers"
            print "There is no car that fits your needs based on passengers"
            return self.__type + " and " + self.__alt_type

    def car_from_mileage(self, mpg):
        m = mpg
        if m > 10 and m < 20:
            self.__type2 = "Muscle"
            self.__alt_type2 = "Sport"
            return self.__type2 + " " + self.__alt_type2
        elif m > 20 and m < 30:
            self.__type2 = "Van"
            self.__alt_type2 = "SUV"
            return self.__type2 + " " + self.__alt_type2
        elif m > 30 and m < 50:
            self.__type2 = "Sedan"
            self.__alt_type2 = "4-Seat Coup"
            return self.__type2 + " " + self.__alt_type2
        else:
            self.__type = "We couldn't find a car for you based on mpg"
            self.__alt_type = "We couldn't find an alternate car for you based on mpg"
            print "There is no car that fits your needs based on passengers"
            return self.__type2 + " and " + self.__alt_type2





