"""
This is the pages class. This will be used to hold all of the html to be displayed later.
There are two parts to this class
self.content which holds the main page with the form that the user will use
self.final_content which holds the results page that will show the users information
"""

class Pages(object):
    def __init__(self):

        """
        self.content

        Below. This is the content that holds the form that the user will input information to
        The user will be asked to input their name, email, number of passengers, desired miles to drive weekly,
        desired gallons of gas that will be used weekly, and whether or not they want to subscribe
        In the form there is a JavaScript function that is passed to it to validate the form.
        See "main.js" for more details
        """

        self.content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>YouCar!</title>
        <link href="css/main.css" rel="stylesheet">
        <script src="js/main.js"></script>
    </head>
    <body>
        <header>
            <h1>Welcome To YouCar!</h1>
        </header>

        <div class="form">
            <form method="GET" action="" onsubmit="return check_input()">
                <h2>Let Us Help You Find A Car</h2>

                <label>Name: </label>
                <input type="text" name="person" id="user">

                <label>Email: </label>
                <input type="text" name="email" id="email">

                <label># Of Passengers: </label>
                <input type="text" name="passenger" id="psgr">

                <h4>Do you want to subscribe to our newsletter?</h4>

                <label id="yes-radio-label">Yes</label>
                <input id="yes-radio" type="radio" name="yesno" value="yes" checked="checked">

                <label id="no-radio-label">No</label>
                <input id="no-radio" type="radio" name="yesno" value="no">

                <h4>Average weekly miles?</h4>
                <select name="miles">
                    <option value="100">100</option>
                    <option value="200">200</option>
                    <option value="400">400</option>
                    <option value="800">800</option>
                </select>
                <h4>Desired Gallons to buy weekly?</h4>
                <select name="gal">
                    <option value="10">10</option>
                    <option value="20">20</option>
                    <option value="30">30</option>
                    <option value="40">40</option>
                </select>

                <input type="submit" value="Submit"/>
            </form>
        </div>
    </body>
</html>
        """

        """
        self.final_content

        Below. This will display the final results to the user through the html that is held here.
        The user will have a list with their name, email, whether or not they subscribed
        Additionally the user will see another list that contains choices of cars based on their preference of miles
        per week and gallons per week.

        """
        self.final_content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>YouCar!</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Your recommendations are below</h1>
        </header>

        <div class="results">
            <div class="result1">
                <h2>Your Information</h2>
                <div class= "info">
                    <h3>Name</h3>
                    <p>{person}</p>
                </div>
                <div class= "info">
                    <h3>Email</h3>
                    <p>{email}</p>
                </div>
                <div class= "info">
                    <h3>Subscribing?</h3>
                    <p>You selected {news} to our newsletter</p>
                </div>
            </div>

            <div class="result2">
                <h2>Your Recommended vehicle is</h2>
                <div class= "info">
                    <h3>You gave us {people} passengers</h3>
                    <p>{cfp}</p>
                </div>
                <div class= "info">
                    <h3>Your minimum mpg is {mpg}</h3>
                    <p>{cfm}</p>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    # This function prints the final page.
    def print_final(self, person, email, news, people, cfm, cfp, mpg):
        final_page = self.final_content     # Simplifying the use of self.final_content
        final_page = final_page.format(**locals())      # formatting the html from the final_page so that the data entered can be used

        # Below, I'm simply returning what was formatted for use in the MainHandler
        return final_page
