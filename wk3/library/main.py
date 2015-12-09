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

        if self.request.GET:
            person = self.request.GET['person']
            email = self.request.GET['email']
            c.passenger = self.request.GET['passenger']
            #news = self.request.GET["yes-no"]
            miles = self.request.GET['miles']
            gal = self.request.GET["gal"]
            print m.mpg(miles, gal)
            self.response.write(p.final_page)
        else:
            self.response.write(p.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
