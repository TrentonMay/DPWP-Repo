"""
name: Trenton May
class: Design Patterns For Web Programming
date: 12/7/2015
assignment: Reusable Libraries
"""
import webapp2
from page import Pages

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages()
        self.response.write(p.content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
