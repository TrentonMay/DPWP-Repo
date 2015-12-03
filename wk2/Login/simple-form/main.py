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
        m = MainPage()

        if self.request.GET:
            person = self.request.GET['person']
            email = self.request.GET['email']
            addy = self.request.GET['address']
            #news = self.request.GET["yes-no"]
            # flavor = self.request.GET['option']
            self.response.write(m.print_final())
        else:
            self.response.write(m.print_main())

class MainPage(object):
    def __init__(self):
        main = MainHandler()
        self.perf = "Bobby"
        self.content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
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
                <select>
                    <option name="option" value="Fruit">Fruit</option>
                    <option name="option" value="Mint">Mint</option>
                    <option name="option" value="Baked">Baked</option>
                    <option name="option" value="Tobacco">Tobacco</option>
                    <option name="option" value="Random">Random</option>
                </select>

                <input type="submit" value="Submit"/>
            </form>
        </div>
    </body>
</html>
        """
        self.final_content1 = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
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
                <p>{self.perf}</p>
            </div>
            <div class= "info">
                <h3>Email</h3>
                <p>{email}</p>
            </div>
            <div class= "info">
                <h3>Shipping to</h3>
                <p>{addy}</p>
            </div>
            """
        self.final_content2 = """
            <div class= "info">
                <h3>Subscribing?</h3>
                <p>You selected {news} to our newsletter</p>
            </div>
            """
        self.final_content3 = """
            <div class= "info">
                <h3>Your Flavor</h3>
                <p>{flavor}</p>
            </div>
        </div>
    </body>
</html>
        """
    def print_main(self):
        page_content = self.content
        page_content = page_content.format(**locals())
        return page_content
    def print_final(self):
        final_page_content = self.final_content1 + self.final_content2 + self.final_content3
        final_page_content = final_page_content.format(**locals())
        return final_page_content


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
