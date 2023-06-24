from lib.menu import *

def test_view_menu_returns_menu_dict():
    menu = Menu()
    assert menu.view_menu() == {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
    }

def test_has_dish_returns_true_when_dish_in_menu():
    menu = Menu()
    assert menu.has_dish("Oxtail") == True

def test_has_dish_returns_false_when_dish_not_in_menu():
    menu = Menu()
    assert menu.has_dish("Escovitch Fish") == False