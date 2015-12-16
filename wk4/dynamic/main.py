
import webapp2
import Pages
import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()
        d = Data.Anime()

        if self.request.GET:
            anime = self.request.GET["anime"]
            print anime
            print d.anime[1]
        else:

            self.response.write(p.Print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
