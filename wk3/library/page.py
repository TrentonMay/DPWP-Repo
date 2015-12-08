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
            <h1>What bike is good for you?</h1>
        </header>

        <div class="form">
            <form method="GET" action="">
                <h2>Your Juice Sheet</h2>

                <label>Name: </label>
                <input type="text" name="person">

                <label>Email: </label>
                <input type="text" name="email">

                <label>Weight: </label>
                <input type="text" name="weight">

                <h4>Do you want to subscribe to our newsletter?</h4>

                <label id="yes-radio-label">Yes</label>
                <input id="yes-radio" type= "radio" name="yes-no" value="yes">

                <label id="no-radio-label">No</label>
                <input id="no-radio" type="radio" name="yes-no" value="no">

                <h4>What is your height?</h4>
                <select name="option">
                    <option value="tall">6' or more</option>
                    <option value="medium">5'8" - 5'11"</option>
                    <option value="average">5'5" - 5'10"</option>
                    <option value="below average">5'0" - 5'4"</option>
                    <option value="short">Below 5'0"</option>
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
        <title>Cycle Dudes</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Your recommended bike is:</h1>
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
                <h3>Size of bike</h3>
                <p>Your Weight is {weight}</p>
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
