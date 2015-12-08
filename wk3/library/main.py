"""
name: Trenton May
class: Design Patterns For Web Programming
date: 12/7/2015
assignment: Reusable Libraries
"""
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
