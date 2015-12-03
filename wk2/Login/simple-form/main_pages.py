class MainPage(object):
    def __init__(self):
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

    def print_content(self):
        return self.content
