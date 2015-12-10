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
            news = self.request.GET['yesno']
            miles = self.request.GET['miles']
            gal = self.request.GET["gal"]

            c.passenger = people
            mpg = m.mpg(miles, gal)
            cfm = f.car_from_mileage(mpg)
            cfp = f.car_from_passengers(int(people))

            print cfm
            print cfp
            self.response.write(p.print_final(person, email, news, people, cfm, cfp, mpg))
        else:
            self.response.write(p.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
