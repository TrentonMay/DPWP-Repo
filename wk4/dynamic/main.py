
import webapp2
import Pages
import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()
        d = Data.Anime()

        if self.request.GET:
            anime = self.request.GET["anime"]
            if anime == "sao":
                a = d.anime[0].title
                print a
            elif anime == "dbz":
                a = d.anime[1].title
                print a
            elif anime == "aot":
                a = d.anime[2].title
                print a
            elif anime == "rk":
                a = d.anime[3].title
                print a
            elif anime == "naruto":
                a = d.anime[4].title
                print a
        else:
            self.response.write(p.Print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
