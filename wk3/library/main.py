"""
name: Trenton May
class: Design Patterns For Web Programming
date: 12/7/2015
assignment: Reusable Libraries
"""
import webapp2
from page import Pages
import lib

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages()
        c = lib.CarData()
        m = lib.CalcMPG()
        f = lib.FinalCar()

        if self.request.GET:
            person = self.request.GET['person']
            email = self.request.GET['email']
            people = self.request.GET['passenger']
            #news = self.request.GET["yes-no"]
            miles = self.request.GET['miles']
            gal = self.request.GET["gal"]

            c.passenger = people
            miles_per = m.mpg(miles, gal)
            car_from_miles = f.car_from_mileage(miles_per)
            car_from_passengers = f.car_from_passengers(int(people))



            print car_from_miles
            print car_from_passengers
            #print m.mpg(miles, gal)
            self.response.write(p.final_page)
        else:
            self.response.write(p.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
