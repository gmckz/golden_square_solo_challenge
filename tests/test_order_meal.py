from lib.order_meal import *
from unittest.mock import Mock
import pytest


def test_initially_order_is_empty_dict():
    my_order = OrderMeal()
    assert my_order.order == {}


def test_add_dish_raises_error_when_nonexistent_dish_added():
    menu = Mock() 
    menu.has_dish.return_value = False
    my_order = OrderMeal()
    with pytest.raises(Exception) as err:
        my_order.add_dish("made up dish", menu)
    error_message = str(err.value)
    assert error_message == "made up dish is not on the menu."


def test_dishes_added_reflected_in_order():
    menu = Mock()
    menu.view_menu.return_value = {
            "Jerk Chicken": 9.95,
            "Oxtail": 12.50,
            "Mac and Cheese": 6.00,
            "Rice and Peas": 5.00
        }
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    assert my_order.order == {"Jerk Chicken": 9.95, "Mac and Cheese": 6.00, "Rice and Peas": 5.00}

def test_confirm_order_raises_error_when_order_empty():
    my_order = OrderMeal()
    with pytest.raises(Exception) as err:
        my_order.confirm_order()
    error_message = str(err.value)
    assert error_message == "Please add dishes to order before confirming."

def test_initially_order_confirmed_false():
    my_order = OrderMeal()
    assert my_order.order_confirmed == False

def test_initially_order_time_set_to_none():
    my_order = OrderMeal()
    assert my_order.order_time == None

def test_confirm_order_sets_order_confirmed_true_when_dishes_added():
    menu = Mock()
    menu.view_menu.return_value = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    my_order.confirm_order()
    assert my_order.order_confirmed == True

def test_confirm_order_sets_order_time_when_dishes_added():
    menu = Mock()
    menu.view_menu.return_value = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    my_order.confirm_order()
    from datetime import datetime
    current_time = datetime.now()
    time_diff = current_time - my_order.order_time 
    assert time_diff.total_seconds() < 1

def test_when_no_dishes_added_grand_total_returns_0():
    my_order = OrderMeal()
    assert my_order.grand_total == 0

def test_when_dishes_added_get_grand_total_returns_correct_amount():
    menu = Mock()
    menu.view_menu.return_value = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    assert my_order.get_grand_total() == "£15.95"

def test_get_itemised_list_returns_order_as_string():
    menu = Mock()
    menu.view_menu.return_value = {
        "Jerk Chicken": 9.95,
        "Oxtail": 12.50,
        "Mac and Cheese": 6.00,
        "Rice and Peas": 5.00
        }
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Oxtail", menu)
    assert my_order.get_itemised_list() == "Jerk Chicken £9.95\nMac and Cheese £6.00\nOxtail £12.50"