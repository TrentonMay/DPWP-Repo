
import webapp2
import Pages
import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()
        d = Data.AnimeData()

        if self.response.GET:
            pass
        else:
            self.reponse.write(p.Print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
