#Objective: The aim of this assignment is to reinforce your understanding and application 
# of Python dictionaries, nested collections, and dictionary methods.


#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu 
# stored in a nested dictionary. Your task is to update this menu based on given instructions

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#- Add a new category called "Beverages" with at least two items.
restaurant_menu["Beverages"] = "sprite", "coke"
print(restaurant_menu)

#- Update the price of "Steak" to 17.99.
restaurant_menu["Steak"] = 17.99
print(restaurant_menu)

#- Remove "Bruschetta" from "Starters". 
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)

