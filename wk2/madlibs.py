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
town_arr2 = ["Dawnstar", "Falkreath", "Markarth", "Morthal", "Riften", "Solitude"]

import random
num1_rand = num1 * random.randrange(1, 3)
num2_rand = num2 * random.randrange(1, 2)

print "Your Story begins!"
print "You are a Knight in the land of" + str(land_name) + ". Your name is" + str(knight_name) + "and you" \
      "serve the king of" + str(king_name) + ". A great Red Dragon by the name of Bahlgore is wreaking havoc" \
      "across the land stealing" + str(pmetal) + "from towns and hoarding them in his dragons den. You set out on " \
      "your quest to figure out how to destroy the dragon once and for all. You know that your sword can not possibly " \
      "penetrate his scales which are as strong as mithril and are" + str(num1) + "inches thick so you set out to find " \
      "Rumplestiltskin, a powerful user of magic that always demands something in return." + str(num2) + "weeks into your " \
      "journey you finally track down Rumple and he agrees to hear your plea for your need to kill Bahlgore, for now. " \
      "He proceeds to tell you that there is no humanly way to kill the dragon but there is a way with magic. He reminds " \
      "you that magic always comes at a price but you proceed anyways. He begins to tell you that the only way to kill " \
      "Bahlgore is to poison it with enchanted meat from a" + str(f_animal) + "and he will give you some in return for a " \
      "golden" + str(f_jewelry) + ". It just so happens that you always carry" + str(num3) + "of them on you and you "\
      "decide to give him one and go on your way to the den of the dragon. Within a few days you make it to the entrance of " \
      "the foul beasts home. You feel the heat from the den as if lava was flowing inside it and you also start to hear some " \
      "sort of deep humming as if there was someone with a deep voice singing a song. As you move deeper into the den you " \
      "start to make out the lyrics to the song."






