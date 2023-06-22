from lib.order_meal import *
from unittest.mock import Mock
import pytest


def test_initially_order_is_empty_dict():
    menu = Mock()
    my_order = OrderMeal(menu)
    assert my_order.order == {}
    assert my_order.menu_obj == menu


# def test_add_dish_raises_error_when_nonexistent_dish_added():
#     menu = Mock(side_effect= "made up dish is not on the menu")
#     menu.add_dish("made up dish") 
#     my_order = OrderMeal(menu)
#     with pytest.raises(Exception) as err:
#         my_order.add_dish("made up dish")
#     error_message = str(err.value)
#     assert error_message == "made up dish is not on the menu."


def test_dishes_added_reflected_in_order():
    menu = Mock()
    menu.menu = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal(menu)
    my_order.add_dish("Jerk Chicken")
    my_order.add_dish("Mac and Cheese")
    my_order.add_dish("Rice and Peas")
    assert my_order.order == {"Jerk Chicken": 9.95, "Mac and Cheese": 6.00, "Rice and Peas": 5.00}

# def test_confirm_order_raises_error_when_order_empty():
#     menu = Mock()
#     my_order = OrderMeal(menu)
#     with pytest.raises(Exception) as err:
#         my_order.confirm_order()
#     error_message = str(err.value)
#     assert error_message == "Please add dishes to order before confirming."

def test_initially_order_confirmed_false():
    menu = Mock()
    my_order = OrderMeal(menu)
    assert my_order.order_confirmed == False

def test_initially_order_time_set_to_none():
    menu = Mock()
    my_order = OrderMeal(menu)
    assert my_order.order_time == None

def test_confirm_order_sets_order_confirmed_true_when_dishes_added():
    menu = Mock()
    menu.menu = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal(menu)
    my_order.add_dish("Jerk Chicken")
    my_order.add_dish("Mac and Cheese")
    my_order.add_dish("Rice and Peas")
    my_order.confirm_order()
    assert my_order.order_confirmed == True

def test_confirm_order_sets_order_time_when_dishes_added():
    menu = Mock()
    menu.menu = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal(menu)
    my_order.add_dish("Jerk Chicken")
    my_order.add_dish("Mac and Cheese")
    my_order.add_dish("Rice and Peas")
    my_order.confirm_order()
    from datetime import datetime
    current_time = datetime.now()
    time_diff = current_time - my_order.order_time 
    assert time_diff.total_seconds() < 1
