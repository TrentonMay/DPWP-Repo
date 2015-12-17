"""
This is the python file where all of the hard coded data is placed
See comments below for more details on each attribute, function, and class
When "Below" is used in the comment it is speaking of the line directly below
"""
# Below, this is the class that will store values from the class below it that inherits from it
# All data is not private so that there can be an openess of information
class AnimeData(object):
    def __init__(self):     # Initializing
        self.title = ""     # Attribute for the title of the anime
        self.image = ""     # Attribute for the image file for the style of the anime
        self.writer = ""        # Attribute for the write of the anime
        self.publisher = ""     # Attribute for the publisher of the anime
        self.director = ""      # Attribute for the director of the anime
        self.episodes = 0       # Attribute for the episodes of the anime
        self.desc = ""      # Attribute for the description of the anime

# Below, this is the Anime class which holds the hard coded data. This inherits from the AnimeData class
class Anime(AnimeData):
    def __init__(self):     # Initializing
        super(AnimeData, self).__init__()   # Constructor function so that the attributes from the super can carry over

        sao = AnimeData()   # Sword Art Online instance
        sao.title = "Sword Art Online"
        sao.image = "css/sao_d.jpg"
        sao.writer = " Reki Kawahara"
        sao.publisher = " ASCII Media Works"
        sao.director = " Tomohiko Ito"
        sao.episodes = 25
        sao.desc = "The year is 2022, and gamers have lined up on launch day for Sword Art Online, a " \
                   "hotly-anticipated MMORPG that lets players connect to an immersive virtual reality " \
                   "world with special helmets called Nerve Gear. Kirito is one such gamer who's eager " \
                   "to jump back into action, having spent a great deal of time as a beta tester, and " \
                   "quickly becomes friends with newbie warrior Klein. But soon, Sword Art Online's 10,000 " \
                   "players discover that not only are they unable to log out, the only way they can return " \
                   "to their physical bodies is by beating the 100-level tower's final boss - death in the " \
                   "game means death in the real world. Now, with no one else to turn to, Kirito and the other " \
                   "participants must survive the game as best they can."

        dbz = AnimeData()   # Dragon Ball Z instance
        dbz.title = "Dragon Ball Z"
        dbz.image = "css/dbz_d.jpg"
        dbz.writer = " Takao Koyama"
        dbz.publisher = " Toei Animation"
        dbz.director = " Shigeyasu Yamauchi"
        dbz.episodes = 291
        dbz.desc = "Goku - the strongest fighter on the planet - is all that stands between humanity and villains " \
                   "from the darkest corners of space. Joined in battle by the Z-Fighters, Goku travels to distant " \
                   "realms in search of the magic powers of the seven Dragon Balls!"

        aot = AnimeData()   # Attack On Titan instance
        aot.title = "Attack On Titan"
        aot.image = "css/aot_d.jpg"
        aot.writer = " Yasuko Kobayashi"
        aot.publisher = " Funimation"
        aot.director = " Tetsuro Araki"
        aot.episodes = 25
        aot.desc = "Known in Japan as Shingeki no Kyojin, many years ago, the last remnants of humanity " \
                   "were forced to retreat behind the towering walls of a fortified city to escape the " \
                   "massive, man-eating Titans that roamed the land outside their fortress. Only the heroic " \
                   "members of the Scouting Legion dared to stray beyond the safety of the walls - but even " \
                   "those brave warriors seldom returned alive. Those within the city clung to the illusion of " \
                   "a peaceful existence until the day that dream was shattered, and their slim chance at survival " \
                   "was reduced to one horrifying choice: kill - or be devoured!"

        rk = AnimeData()    # Rurouni Kenshin instance
        rk.title = "Rurouni Kenshin"
        rk.image = "css/rk_d.jpg"
        rk.writer = " Mari Okada"
        rk.publisher = " Aniplex"
        rk.director = " Kazuhiro Furuhashi"
        rk.episodes = 95
        rk.desc = 'Welcome to the Meiji Era. Japan is a land experiencing times of troubled peace and renewal ' \
                  'after a long and bloody civil war. Swords and killing are outlawed, but all is not as well as ' \
                  'it would seem. Lurking in the shadows are many survivors of the revolution awaiting their chance ' \
                  'for vengeance. Only the former government assassin, Kenshin Himura can keep the peace. Kenshin ' \
                  'gives up the life of "Battousai The Man Slayer" and sets off as a lone wanderer. His travels lead ' \
                  'to the Kamiya Dojo where he discovers the chance to start life over'

        naruto = AnimeData()    # naruto instance
        naruto.title = "Naruto"
        naruto.image = "css/naruto_d.jpg"
        naruto.writer = " Masashi Kishimoto"
        naruto.publisher = " TV TOKYO"
        naruto.director = " Hayato Date"
        naruto.episodes = 661
        naruto.desc = "Many years ago, in the hidden village of Konoha, lived a great demon fox. When it swung " \
                      "one of it's nine tails, a tsunami occurred. The fourth hokage sealed this demon fox inside " \
                      "a boy in exchange for his own life. Naruto was that boy, and he grew up with no family, and " \
                      "the villagers hated him thinking that he himself was the demon fox. Naruto's dream is to become " \
                      "Hokage, and have the villagers acknowledge him"
        # Below, storing the instances above in an array so that they may be easily accessed in other files
        self.anime = [sao, dbz, aot, rk, naruto]

