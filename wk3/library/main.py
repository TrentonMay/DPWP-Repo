"""
name: Trenton May
class: Design Patterns For Web Programming
date: 12/7/2015
assignment: Reusable Libraries
"""
import webapp2
from page import Pages  # Importing the page class to be printed to the view
import lib  # importing everything from the library. This is because everything from the library is being used

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages()  # assigning the pages class to a variable for ease of use and readability
        c = lib.CarData()   # assigning the CarData class to a variable for ease of use and readability
        m = lib.CalcMPG()   # assigning the CalcMpg class to a variable for ease of use and readability
        f = lib.FinalCar()  # assigning the FinalCar class to a variable for ease of use and readability

        if self.request.GET:    # If there was information gathered then run the following code
            person = self.request.GET['person']     # Getting the data that the user entered. This is their name
            email = self.request.GET['email']       # This is their email
            people = self.request.GET['passenger']      # This the number of passengers
            news = self.request.GET['yesno']        # This is whether or not they are subscribing
            miles = self.request.GET['miles']       # This is how many miles they plan on going in a week
            gal = self.request.GET["gal"]       # This is how many gallons they plan on using in a week

            c.passenger = people    # calling a function. Passing the number of passengers into it
            mpg = m.mpg(miles, gal)     # this gets the mpg by using the mpg function. Passing miles and gallons to it
            cfm = f.car_from_mileage(mpg)   # determining the choice of cars by mileage
            cfp = f.car_from_passengers(int(people))    # determining the choice of cars by passengers

            """
            The below line prints the html to the console. It takes this many parameters to the function so that these
            values can be used in the html in the pages class to displayed to the user
            """
            self.response.write(p.print_final(person, email, news, people, cfm, cfp, mpg))
        else:
            self.response.write(p.content)  # If there was no information gathered then it will display the first view

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
