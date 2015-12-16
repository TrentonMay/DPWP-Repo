
import webapp2
import Pages
import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()
        d = Data.AnimeData()

        if self.response.GET:
            pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
