"""
Trenton May
12/2/15
Design Patterns For Web Programming
Simple Form
"""
import webapp2
# from main_pages import MainPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Setting a variable so that I may access the MainPage class here in the Handler
        m = MainPage()

        # This if statement allows me to validate whether or not there was anything received
        # If true it will catch the data and store it in the following variables for ease of use
        if self.request.GET:
            person = self.request.GET['person']     # Gets the data from the Name text field
            email = self.request.GET['email']       # Gets the data from the Email text field
            addy = self.request.GET['address']      # Gets the data from the Address text field
            news = self.request.GET["yes-no"]       # Gets the data from the Subscription radio buttons
            flavor = self.request.GET['option']     # Gets the data from the selection box

            # Below, writes the html to the page so that it can be viewed by the user
            # In order to display the data, these variables needed to be passed to the function for print_final
            # Without these arguments I can't access the data from the variables
            self.response.write(m.print_final(person, email, addy, news, flavor))

            # Below, This is just for my own personal use to check if the form was working
            print person + email + addy + news + flavor
            # Below, if the above statement is false and nothing was entered the original page will print
        else:
            self.response.write(m.print_main())

# This class is used to hold the content of the pages and the print functions.
class MainPage(object):
    def __init__(self):
        # Below is the main content where the user will input their order
        self.content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Juice Order Form</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Vape Juice Order Form</h1>
        </header>

        <div class="main-form">
            <form method="GET" action="">
                <h2>Your Juice Sheet</h2>

                <label>Name: </label>
                <input type="text" name="person">

                <label>Email: </label>
                <input type="text" name="email">

                <label>Address: </label>
                <input type="text" name="address">

                <h4>Do you want to subscribe to our newsletter?</h4>

                <label id="yes-radio-label">Yes</label>
                <input id="yes-radio" type= "radio" name="yes-no" value="yes">

                <label id="no-radio-label">No</label>
                <input id="no-radio" type="radio" name="yes-no" value="no">

                <h4>What is your favorite flavor?</h4>
                <select name="option">
                    <option value="Fruit">Fruit</option>
                    <option value="Mint">Mint</option>
                    <option value="Baked">Baked</option>
                    <option value="Tobacco">Tobacco</option>
                    <option value="Random">Random</option>
                </select>

                <input type="submit" value="Submit"/>
            </form>
        </div>
    </body>
</html>
        """
        # This is the final print of the content that will be displayed
        # There are multiple lines that access the information from the handler class
        # They are wrapped in brackets
        self.final_content1 = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Juice Order Form</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Your Order Is On Its Way!</h1>
        </header>

        <div class="result">
            <h2>Your Order</h2>
            <div class= "info">
                <h3>Name</h3>
                <p>{person}</p>
            </div>
            <div class= "info">
                <h3>Email</h3>
                <p>{email}</p>
            </div>
            <div class= "info">
                <h3>Shipping to</h3>
                <p>{addy}</p>
            </div>
            <div class= "info">
                <h3>Subscribing?</h3>
                <p>You selected {news} to our newsletter</p>
            </div>
            <div class= "info">
                <h3>Your Flavor</h3>
                <p>{flavor}</p>
            </div>
        </div>
    </body>
</html>
        """
        # This print is for the main page for the form where the user will enter the information
    def print_main(self):

        # Below I'm putting the page content in a variable to make this easier to code
        page_content = self.content

        # Below, I'm formatting the content from html so that it can accept variables in this format {self.x} or {x}
        page_content = page_content.format(**locals())

        # Below I'm making this function simply return what was formatted
        return page_content

        # Below, I need to pass these arguments into the function to access instance variables from MainHandler
        # Without this I can't access the variables to be placed in the html.
        # This is the final print that will display the users information
    def print_final(self, person, email, addy, news, flavor):

        # Below, I'm putting the final content in a variable for ease of use
        final_page_content = self.final_content1

        # Below, I'm formatting the content from html so that it can accept variables in the html
        # Without this it just simply displays what I enter as text
        final_page_content = final_page_content.format(**locals())
        
        # Below, I'm simply returning what was formatted for use in the MainHandler
        return final_page_content


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
