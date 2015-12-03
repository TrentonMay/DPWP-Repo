class MainPage(object):
    def __init__(self):
    def get(self):
        self.content = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Information For registration</h1>
        </header>

        <div class="main-form">
            <form method="GET" action="">
                <h2>Basic Information</h2>

                <label>Task: </label>
                <input type="text" name="task">

                <label>Due Time: </label>
                <input type="text" name="due">

                <label>Status: </label>
                <input type="text" name="status">

                <h4>Do you want to subscribe to our newsletter?</h4>

                <label id="yes-radio-label">Yes</label>
                <input id="yes-radio" type= "radio" name="yes" value="yes">

                <label id="no-radio-label">No</label>
                <input id="no-radio" type="radio" name="no" value="no">

                <h4>What is your favorite sport?</h4>
                <select>
                    <option value="Football">Football</option>
                    <option value="Ultimate Frisbee">Ultimate Frisbee</option>
                    <option value="Soccer">Soccer</option>
                    <option value="Hockey">Hockey</option>
                    <option value="Baseball">Baseball</option>
                    <option value="Rugby">Rugby</option>
                </select>

                <input type="submit" value="Submit"/>
            </form>
        </div>
    </body>
</html>
        """
        if self.request.GET:
            print self.request.GET['task']

    def print_content(self):
        return self.content
