"""
Trenton May
12/2/15
Design Patterns For Web Programming
Simple Form
"""
import webapp2
"""
Was going to import the page from another python file but for some reason the
GET method wouldn't work that way so I had to revert to a simpler code design
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = """
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
                    <option name="option" value="Football">Football</option>
                    <option name="option" value="Ultimate Frisbee">Ultimate Frisbee</option>
                    <option name="option" value="Soccer">Soccer</option>
                    <option name="option" value="Hockey">Hockey</option>
                    <option name="option" value="Baseball">Baseball</option>
                    <option name="option" value="Rugby">Rugby</option>
                </select>

                <input type="submit" value="Submit"/>
            </form>
        </div>
    </body>
</html>
        """

        if self.request.GET:
            person = self.request.GET['person']
            email = self.request.GET['email']
            addy = self.request.GET['address']
            news = self.request.GET["yes-no"]
            #flavor = self.request.GET['option']
            self.response.write(final_content1 + final_content2 + final_content3)
        else:
            self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
