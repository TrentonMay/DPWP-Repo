
import webapp2
import Pages
import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()
        p2 = Pages.FinalPage()
        d = Data.Anime()

        if self.request.GET:
            anime = self.request.GET["anime"]
            if anime == "sao":
                a = d.anime[0]
                self.response.write(p2.print_out(a))
            elif anime == "dbz":
                a = d.anime[1]
                self.response.write(p2.print_out(a))
            elif anime == "aot":
                a = d.anime[2]
                self.response.write(p2.print_out(a))
            elif anime == "rk":
                a = d.anime[3]
                self.response.write(p2.print_out(a))
            elif anime == "naruto":
                a = d.anime[4]
                self.response.write(p2.print_out(a))
        else:
            a = d.anime
            self.response.write(p.print_out(a))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
