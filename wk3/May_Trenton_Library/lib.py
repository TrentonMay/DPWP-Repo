"""
This is the library
Contains
CarData: This is a class used to receive the data for the passengers
CalcMPG: This is used to calculate the miles per gallon
FinalCar: This is used to output the final cars to the html

see more one line comments below
Any comment referring to "Below" is pointing to the line directly below.
"""

class CarData(object):
    def __init__(self):
        self.__passenger = ""   # Setting the private attribute to an empty string so it can receive a value

    @property
    def passenger(self):    # creating a function to simply return the private passenger attribute
        return self.__passenger
    @passenger.setter
    def passenger(self, x):     # This function is going to receive the number of passengers from the mainhandler
        if int(x) > 8:  # Saying if the number of passengers is larger than 8
            # Then tell the terminal that there is no car that holds this many people
            print "There is no production vehicle that holds this many people"
        else:
            self.__passenger = x    # if the passenger number is less than 8 then set self.__passenger to that number



class CalcMPG(object):
    def __init__(self):
        self.__final_mpg = 0    # creating a private attribute to output the final mpg to to store the data

    def mpg(self, miles, gal):  # This function will calculate the mpg to be used later, takes number of miles and gas
        num_miles = int(miles)  # using a variable to make sure that the miles inputted is an integer
        num_gal = int(gal)      # using a variable to make sure that the gas inputted is an integer

        final_mpg = num_miles / num_gal     # Using simple math to get the mpg and storing it in a variable
        # Below. Print to the console the miles per gallon
        print "Your mpg is " + str(final_mpg) + " miles per gallon"
        self.__final_mpg = final_mpg    # making the private attribute equal to the final miles per gallon
        return final_mpg    # Returning the miles per gallon

class FinalCar(object):
    def __init__(self):
        self.__type = ""    # using a private attribute to hold the first primary car type
        self.__alt_type = ""    # using a private attribute to hold the first secondary car type
        self.__type2 = ""   # using a private attribute to hold the second primary car type
        self.__alt_type2 = ""   # using a private attribute to hold the second secondary car type



    def car_from_passengers(self, people):
        x = people  # making x equal to people so that the statements below can be less cluttered

        if x == 1 or x == 0:    # Saying if the number of passengers is equal to 1 or 0 then run this code
            self.__type = "Muscle"  # if the statement is true then self.__type will be equal to Muscle
            self.__alt_type = "Sport"   # if the statement is true then self.__alt_type will be equal to sport
            # Below. Returning this string with the selected cars to be used in the html
            return "Based on this we recommend you get a " + self.__type + " or " + self.__alt_type + " car"
        elif x < 8 and x > 3:   # Saying if the number of passengers is less than 8 or more than 3 then run this code
            self.__type = "Van"     # if the statement is true then self.__type will be equal to Van
            self.__alt_type = "SUV"     # if the statement is true then self.__alt_type will be equal to SUV
            # Below. Returning this string with the selected cars to be used in the html
            return "Based on this we recommend you get a " + self.__type + " or " + self.__alt_type
        elif x > 1 and x < 4:   # Saying if the number of passengers is more than 1 or less than 4 then run this code
            self.__type = "Sedan"   # if the statement is true then self.__type will be equal to Sedan
            self.__alt_type = "4-Seat Coup"     # if the statement is true then self.__alt_type will be equal to Coup
            # Below. Returning this string with the selected cars to be used in the html
            return "Based on this we recommend you get a " + self.__type + " or " + self.__alt_type
        else:  # if everything above is false then run this
            # Below. This will let the user know we couldn't find a car for them
            self.__type = "We couldn't find a car for you based on passengers"
            # Below. This will let the user know we couldn't find an alternate car for them
            self.__alt_type = "we couldn't find an alternate car for you based on passengers"
            print "There is no car that fits your needs based on passengers"
            # Below. Will return the above statements so the user will be notified
            return self.__type + " and " + self.__alt_type

    def car_from_mileage(self, mpg):
        m = mpg     # setting m equal to mpg for simplification of the following statements
        if m > 7 and m < 20:    # if m is more than 7 and less than 20 then run this code
            self.__type2 = "Muscle"
            self.__alt_type2 = "Sport"
            return "Based on this we recommend you get a " + self.__type2 + " or " + self.__alt_type2 + " car"
        elif m > 19 and m < 30:     # if m is more than 19 and less than 30 then run this code
            self.__type2 = "Van"
            self.__alt_type2 = "SUV"
            return "Based on this we recommend you get a " + self.__type2 + " or " + self.__alt_type2
        elif m > 29 and m < 60:     # if m is more than 29 and less than 60 then run this code
            self.__type2 = "Sedan"
            self.__alt_type2 = "4-Seat Coup"
            return "Based on this we recommend you get a " + self.__type2 + " or " + self.__alt_type2
        elif m > 59:        # if m is more than 59
            self.__type2 = "primary type"   # setting the type2 to primary type so that it can be used in the return
            # Below. Setting the alt_type2 to primary type so that it can be used in the return
            self.__alt_type2 = "secondary type"
            # Below. This returns the information necessary to tell the user that no car is this efficient
            return "We're sorry there was no " + self.__type2 + " or " + self.__alt_type2 + " that is that efficient"
        else:       # if everything above is false then run this
            # Below. This will let the user know we couldn't find a car for them
            self.__type2 = "We couldn't find a car for you based on mpg"
            # Below. This will let the user know we couldn't find an alternate car for them
            self.__alt_type2 = "we couldn't find an alternate car for you based on mpg"
            print "There is no car that fits your needs based on mileage"
            # Below. Will return the above statements so the user will be notified
            return self.__type2 + " and " + self.__alt_type2





