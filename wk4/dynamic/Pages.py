class Page(object):
    def __init__(self):
        self.nav = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <link href="css/main.css" rel="stylesheet">

</head>
<body>
    <nav>
        <ul>
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
        self.end = """
</body>
</html>
        """
    def Print_out(self):
        return self.nav + self.end

class FinalPage(Page):
    def __init__(self):
        super(Page, self).__init__()
        self.final = """
    <div class="display" style="background-image: url('{}')">
        <h1>{}</h1>
        <div class="info">
            <ul>
                <li><p>Seasons:{}</p></li>
                <li><p>Publisher:{}</p></li>
                <li><p>Written By:{}</p></li>
                <li><p>Director:{}</p></li>
            </ul>
        </div>
        <div class="desc">
            <h2>Description</h2>
            <p>{}</p>
        </div>
    </div>
        """

