class Pages(object):
    def __init__(self):
        self.content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Cycle Dudes</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>YouCar @copy</h1>
        </header>

        <div class="form">
            <form method="GET" action="">
                <h2>Your Recommended Car</h2>

                <label>Name: </label>
                <input type="text" name="person">

                <label>Email: </label>
                <input type="text" name="email">

                <label># Of Passengers: </label>
                <input type="text" name="passenger">

                <h4>Do you want to subscribe to our newsletter?</h4>

                <label id="yes-radio-label">Yes</label>
                <input id="yes-radio" type= "radio" name="yes-no" value="yes">

                <label id="no-radio-label">No</label>
                <input id="no-radio" type="radio" name="yes-no" value="no">

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
        self.final_page = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>YouCar</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Your recommendations are below</h1>
        </header>

        <div class="result">
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
            <div class= "info">
                <h3>You gave us {passenger} passengers</h3>
                <p>Based on this we recommend you get a {car_from_passengers}</p>
            </div>
            <div class= "info">
                <h3>Your minimum mpg is {mpg}</h3>
                <p>Based on this we recommend you get a {car_from_miles}</p>
            </div>
        </div>
    </body>
</html>
"""
