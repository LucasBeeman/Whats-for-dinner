import random


ethnicity = [0, 1, 2, 3]
type_choice = -1
user_choice = input("Which ethnnic resturaunt would you like to eat at? Italian(1), Indian(2), Chinese(3), Middle Eastern(4), Don't know(5)")
if user_choice.strip() == "5":
    type_choice = random.choice(ethnicity)
if type_choice == 0 or user_choice.strip() == "1":
    ethnicity = "italian"
    place = ["Bruno Bros", "Belleria", "Bella Napoli"]
elif type_choice == 1 or user_choice.strip() == "2":
    ethnicity = "Indian"
    place = ["Cafe India", "Bombay Curry and Grill", "Kabab and Curry"]
elif type_choice == 2 or user_choice.strip() == "3":
    ethnicity = "Chinese"
    place = ["Main Moon", "Hunan Express", "Imperial Graden"]
elif type_choice == 3 or user_choice.strip() == "4":
    ethnicity = "Middle Eastern"
    place = ["Zenobia", "Ghossain's", "sauceino"]
else:
    print("ERROR")
if type_choice is not -1:
    print("your ethnicity is", ethnicity)
place_choice = random.choice(place)
print("your going to", str(place_choice) + "!")