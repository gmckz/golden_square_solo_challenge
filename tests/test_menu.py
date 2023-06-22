from lib.menu import *

def test_view_menu_returns_menu_dict():
    menu = Menu()
    assert menu.view_menu() == {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
    }
