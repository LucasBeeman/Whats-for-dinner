import random

ethnicity = [0, 1, 2, 3, 4]
type_choice = random.choice(ethnicity)

if type_choice == 0:
    ethnicity = "italian"
    place = ["Bruno Bros", "Belleria", "Bella Napoli"]
elif type_choice == 1:
    ethnicity = "Indian"
    place = ["Cafe India", "Bombay Curry and Grill", "Kabab and Curry"]
elif type_choice == 2:
    ethnicity = "Chinese"
    place = ["Main Moon", "Hunan Express", "Imperial Graden"]
elif type_choice == 3:
    ethnicity = "Middle Eastern"
    place = ["Zenobia", "Ghossain's", "sauceino"]
elif type_choice == 4:
    ethnicity = "Mix"
    place = ["Bruno Bros", "Belleria", "Bello Napoli", "Cafe India", "Bambay Curry and Grill", "Kabab and Curry", "Main Moon", "Hunan Express", "Imperial Graden", "Zenobia", "Ghossain's", "sauceino"]
print("The ethnicity is", ethnicity)

place_choice = random.choice(place)
print("your going to", str(place_choice) + "!")