print "Before your story begins"
knight_name = raw_input("Enter your Knightly Name ")
land_name = raw_input("Enter the name of your medieval country ")
king_name = raw_input("Enter the name of your King ")
pmetal = raw_input("What's your favorite precious metal? ")
f_animal = raw_input("What's your favorite animal? ")
f_jewelry = raw_input("What's your favorite piece of jewelry ")
num1 = raw_input("Enter a number between 0-5 ")
num2 = raw_input("Enter a number between 5-10 ")
num3 = raw_input("Enter a number between 10-15 ")

town_arr = ["Ghanshire", "Steadholme", "Ravenwood", "Riveton", "Alefast", "Nahrsong"]
town_dict = dict()
town_dict = {"Skyrim":"Dawnstar", "LOTR":"Archet", "GOT":"Winterfell", "Oblivion":"Cyrodil", "ESO":"Mathiisen", "Vikings":"Kattegat"}

import random
num2_rand = num2 * random.randrange(1, 2)

def calcConclusion(num2_rand, num1):
    final = num2_rand / num1
    return final
print calcConclusion(num2_rand, num1)

print "Your Story begins!"
print "You are a Knight in the land of " + str(land_name) + ". Your name is " + str(knight_name) + " and you " \
      "serve the king of " + str(king_name) + ". A great Red Dragon by the name of Bahlgore is wreaking havoc " \
      "across the land stealing " + str(pmetal) + " from towns and hoarding them in his dragons den. You set out on " \
      "your quest to figure out how to destroy the dragon once and for all. You know that your sword can not possibly " \
      "penetrate his scales which are as strong as mithril and are " + str(num1) + " inches thick so you set out to find " \
      "Rumplestiltskin, a powerful user of magic that always demands something in return. " + str(num2) + " weeks into your " \
      "journey you finally track down Rumple and he agrees to hear your plea for your need to kill Bahlgore, for now. " \
      "He proceeds to tell you that there is no humanly way to kill the dragon but there is a way with magic. He reminds " \
      "you that magic always comes at a price but you proceed anyways. He begins to tell you that the only way to kill " \
      "Bahlgore is to poison it with enchanted meat from a " + str(f_animal) + " and he will give you some in return for a " \
      "golden " + str(f_jewelry) + ". It just so happens that you always carry " + str(num3) + " of them on you and you "\
      "decide to give him one and go on your way to the den of the dragon. Within a few days you make it to the entrance of " \
      "the foul beasts home. You feel the heat from the den as if lava was flowing inside it and you also start to hear some " \
      "sort of deep humming as if there was someone with a deep voice singing a song. As you move deeper into the den you " \
      "start to make out the lyrics to the song. "

print "Up in the sky I see down below"
for i in range(0,3):
    print "Below"
    i = i+1
    pass
print "Air beneath my wings with a burning"
for i in range(0,3):
    print "Flow"
    i = i+1
    pass
print "You can't best a dragon don't you know"
for i in range(0,3):
    print "Know"
    i = i+1
    pass

print "Bahlgore then begins to name the towns he has burned only to ignite the hatred in your heart even more"

if num1 > 3:
    print town_arr[0]
    print town_arr[1]
    print town_arr[2]
    print town_arr[3]
    print town_arr[4]
    print town_arr[5]
else:
    print town_dict["Skyrim"]
    print town_dict["LOTR"]
    print town_dict["GOT"]
    print town_dict["Oblivion"]
    print town_dict["ESO"]
    print town_dict["Vikings"]
    pass

print "His deep voice sends chills down your spine but you move forward anyways to as far as you an go without being in sight of the " \
      "beast. You see the beast and how he towers above you like a giant. Even though you are trembling with fear you spot where he keeps " \
      "his pile of fresh meat for eating and place the enchanted" + str(f_animal) + "meat in the pile. You wait in a corner for what " \
      "feels like an eternity until finally you hear a familiar rumbling that echoes throughout the den. Bahlgore, aware of his own rumbling " \
      "stomach reaches for his pile of meat with his long taloned hands and torches his meat to perfection and gulps down the meal unknowing of " \
      "the enchanted meat in the midst of his dinner. In a blink of an eye the dragon shrinks to the size of a cat. You know you'll never get a " \
      "better shot at killing the wretched beast so you move in and slice off his head with one clean swipe of your sword. Immediately you travel " \
      "back to the kingdom to claim your reward and your honor"






