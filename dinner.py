import random


ethnicity = [0, 1, 2, 3]
type_choice = -1
user_choice = input("Which ethnnic resturaunt would you like to eat at? Italian(1), Indian(2), Chinese(3), Middle Eastern(4), Don't know(5)")
#if the user pick I dont know, the code will pick one for them through randomness
if user_choice.strip() == "5":
    type_choice = random.choice(ethnicity)
#change "ethnicity" to a string stating what the ethnicity is, this is for the print later on. add a list of at least 3 rasturants of that ethnicity
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
#error handeling
else:
    print("ERROR")
#if the user said that they don't know, state what ethnicity the resturant is
if type_choice is not -1:
    print("your ethnicity is", ethnicity)
#prints the random reasturaunt from the list of 3 resturants, then prints it out
place_choice = random.choice(place)
print("your going to", str(place_choice) + "!")