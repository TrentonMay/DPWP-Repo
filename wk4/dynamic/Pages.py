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
    <div id= "home-body" style="background-image: url('css/home.jpg')">
        <div id="h-desc">
            <h1>Welcome to A-World</h1>
            <p>Choose Any Anime To Find Out More Information</p>
        </div>
    </div>
</body>
</html>
        """
    def print_out(self, a):
        print a
        return self.nav + self.end

class FinalPage(Page):
    def __init__(self):
        super(FinalPage, self).__init__()

        self.final = """
    <div class="display" style="background-image: url('{a.image}')">
        <h1>{a.title}</h1>
        <div class="info">
            <ul>
                <li><p>Seasons:{a.episodes}</p></li>
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
    def print_out(self, a):
        final = self.final.format(**locals())
        return self.nav + final + self.end

