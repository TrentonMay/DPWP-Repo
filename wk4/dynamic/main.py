"""
This is the main python file that holds the Main Handler
See single line comments below to find out more about the classes, attributes and functions
When "below" is used it is referring to the line directly below
"""
import webapp2  # Importing webapp2
import Pages    # Importing everything from Pages.py since everything needs to be used
from Data import Anime    # Importing Anime from Data.py since that's all that needs to be used

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Pages.Page()    # Setting an attribute equal to the Page class. There are specific things from this needed
        p2 = Pages.FinalPage()  # Setting an attribute equal to the FinalPage class
        d = Anime()     # Setting an attribute equal to the Anime class from Data.py
        # Below, Setting the anime attribute equal to an empty string so that it can be accessed by the else statement
        # This is needed so that the polymorphic function can receive the data it needs from its parameter
        self.anime = ""

        if self.request.GET:    # If there was information entered then do the following:
            self.anime = self.request.GET["anime"]      # Setting self.anime equal to the information inputted
            if self.anime == "sao":     # If the anime is equal to Sword Art Online then do the following:
                a = d.anime[0]  # Setting a equal to the appropriate data for this view
                self.response.write(p2.print_out(a, self.anime))    # using the appropriate print function
            elif self.anime == "dbz":   # If the anime is equal to Dragon Ball Z then do the following:
                a = d.anime[1]  # Setting a equal to the appropriate data for this view
                self.response.write(p2.print_out(a, self.anime))    # using the appropriate print function
            elif self.anime == "aot":   # If the anime is equal to Attack On Titan then do the following:
                a = d.anime[2]  # Setting a equal to the appropriate data for this view
                self.response.write(p2.print_out(a, self.anime))    # using the appropriate print function
            elif self.anime == "rk":    # If the anime is equal to Rurouni Kenshin then do the following:
                a = d.anime[3]  # Setting a equal to the appropriate data for this view
                self.response.write(p2.print_out(a, self.anime))    # using the appropriate print function
            elif self.anime == "naruto":    # If the anime is equal to Naruto then do the following:
                a = d.anime[4]  # Setting a equal to the appropriate data for this view
                self.response.write(p2.print_out(a, self.anime))    # using the appropriate print function
            else:   # if none of the above statements are true then it will go to the home page
                a = d.anime     # Setting a equal to the data array so that it can be printed to the log
                self.response.write(p.print_out(a, self.anime)) # using the appropriate print function
        else:   # if there was no information inputted then it will go to the home page
            a = d.anime     # Setting a equal to the data array so that it can be printed to the log
            self.response.write(p.print_out(a, self.anime)) # using the appropriate print function

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
