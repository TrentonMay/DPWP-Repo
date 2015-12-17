"""
This is Pages.py where all of the html will be stored for use in the main handler
Further information is said below in single line comments
When a comment says "Below" it is referring to the line directly below
See below to find out more about each function, class, and attribute
"""

# Below, This page class holds the main content that is a basis for the application
class Page(object):
    def __init__(self):  # Intiializing
        # Below, This is the navigation styles that holds the links to other views or "pages"
        self._nav = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Anime World</title>
    <link href="css/main.css" rel="stylesheet">

</head>
<body>
    <nav>
        <ul>
            <li>
                <a href = "?anime=home"><img src="css/home_icon.png"></a>
            </li>
            <li>
                <a href = "?anime=sao"><img src="css/sao_icon.png"></a>
            </li>
            <li>
                <a href = "?anime=aot"><img src="css/aot_icon.png"></a>
            </li>
            <li>
                <a href = "?anime=dbz"><img src="css/dbz_icon.png"></a>
            </li>
            <li>
                <a href = "?anime=naruto"><img src="css/naruto_icon.png"></a>
            </li>
            <li>
                <a href = "?anime=rk"><img src="css/rk_icon.png"></a>
            </li>
        </ul>
    </nav>
    """
        # Below, This is the end tag to complete the html by closing the body and html tags
        self._end = """
</body>
</html>
        """
        # Below, this is a function that will decide if it should display the home screen styles and html
        # Basically this function is adding another level of assurance
        # This ensures that in no way shape or form will the wrong page be displayed
        # Below in the other class that inherits from Page, this is overwritten
    def home_display(self, anime):
        if anime == "home" or anime == "":  # If the link is equal to home or nothing then do the following:
            # Below, this is the html that will be injected if the link is equal to home
            home = """
    <div id= "home-body" style="background-image: url('css/home.jpg')">
        <div id="h-desc">
            <h1>Welcome to Ani-World</h1>
            <p>Choose Any Anime To Find Out More Information</p>
        </div>
    </div>
    """
            return home     # Returning the above html
        else:   # If the above statement is false and it is anything else then return the following:
            home = ""
            return home     # Basically return nothing this is in case the user is not clicking home
    # Below, this is just a basic print function that takes the function home as an argument to display the correct html
    # This is also rewritten below
    def print_out(self, a, anime):
        print a  # This is just printing to the console so that you can confirm the data is there
        # Below, This concatenates the nav and the end but also the home html if it's needed.
        return self._nav + self.home_display(anime) + self._end

# Below, this class is for the final output of each view so that everything is displayed correctly according to the link
# This inherits from Page
class FinalPage(Page):
    def __init__(self):     # Initializing
        super(FinalPage, self).__init__()   # Constructor function so that attributes carry over
    # Below, Overriding the above home function
    # This is needed because it needs basically the same html as above but it needs it to be a little different
    # This allows for more assurance so that the correct view is ALWAYS displayed
    def home_display(self, anime):
        if anime == "home":     # Saying if the link is equal to home then do the following
            # Below, making final equal to the home html so that the user knows they are at the home page
            final = """
    <div id= "home-body" style="background-image: url('css/home.jpg')">
        <div id="h-desc">
            <h1>Welcome to Ani-World</h1>
            <p>Choose Any Anime To Find Out More Information</p>
        </div>
    </div>
    """
            return final        # returning the html to be outputted
        else:       # If the link doesn't equal home then do the following
            # Below, setting final equal to dynamic html that will take values from the database
            final = """
    <div class="display" style="background-image: url('{a.image}')">
        <h1>{a.title}</h1>
        <div class="info">
            <ul>
                <li><p>Episodes:{a.episodes}</p></li>
                <li><p>Publisher:{a.publisher}</p></li>
                <li><p>Written By:{a.writer}</p></li>
                <li><p>Director:{a.director}</p></li>
            </ul>
        </div>
        <div class="desc">
            <h2>Description</h2>
            <p>{a.desc}</p>
        </div>
    </div>
        """
            return final    # Returning the html to be outputted

    # Below, this is a basic print function that overrides the above one because it needs what the other doesn't
    # This also takes the home function from above to decide if it needs the home page or the different views
    def print_out(self, a, anime):
        # Below, Formatting the html in the home function while also setting it to a variable to be used in the print
        # It is formatted so that it can take in the data from the array in Data.py
        final = self.home_display(anime).format(**locals())
        # Below, returning the html from above. Nav and End both come from the Page class
        return self._nav + final + self._end

