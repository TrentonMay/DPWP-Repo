class Page(object):
    def __init__(self):
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
        self._end = """
</body>
</html>
        """
    def home_display(self, anime):
        if anime == "home":
            home = """
    <div id= "home-body" style="background-image: url('css/home.jpg')">
        <div id="h-desc">
            <h1>Welcome to Ani-World</h1>
            <p>Choose Any Anime To Find Out More Information</p>
        </div>
    </div>
    """
            return home
        else:
            home = ""
            return home

    def print_out(self, a, anime):
        print a
        return self._nav + self.home_display(anime) + self._end

class FinalPage(Page):
    def __init__(self):
        super(FinalPage, self).__init__()
    def home_display(self, anime):
        if anime == "home":
            final = """
    <div id= "home-body" style="background-image: url('css/home.jpg')">
        <div id="h-desc">
            <h1>Welcome to Ani-World</h1>
            <p>Choose Any Anime To Find Out More Information</p>
        </div>
    </div>
    """
            return final
        else:
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
            return final

    def print_out(self, a, anime):
        final = self.home_display(anime).format(**locals())
        return self._nav + final + self._end

