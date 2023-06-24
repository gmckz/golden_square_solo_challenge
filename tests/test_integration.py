from lib.menu import *
from lib.order_meal import *
from lib.receipt import *
import pytest


def test_add_dish_raise_error_when_nonexistent_dish_added():
    menu = Menu()
    my_order = OrderMeal()
    with pytest.raises(Exception) as err:
        my_order.add_dish("made up dish", menu)
    error_message = str(err.value)
    assert error_message == "made up dish is not on the menu."

def test_dishes_added_reflected_in_order():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    assert my_order.order == {"Jerk Chicken": 9.95, "Mac and Cheese": 6.00, "Rice and Peas": 5.00}

def test_confirm_order_raises_error_when_order_empty():
    menu = Menu()
    my_order = OrderMeal()
    with pytest.raises(Exception) as err:
        my_order.confirm_order()
    error_message = str(err.value)
    assert error_message == "Please add dishes to order before confirming."

def test_confirm_order_sets_order_confirmed_true_when_dishes_added():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    my_order.confirm_order()
    assert my_order.order_confirmed == True

def test_confirm_order_sets_order_time_when_dishes_added():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Rice and Peas", menu)
    my_order.confirm_order()
    from datetime import datetime
    current_time = datetime.now()
    time_diff = current_time - my_order.order_time 
    assert time_diff.total_seconds() < 1

def test_when_order_not_confirmed_view_receipt_raises_error():
    menu = Menu()
    my_order = OrderMeal()
    my_receipt = Receipt()
    with pytest.raises(Exception) as err:
        my_receipt.view_receipt(my_order)
    error_message = str(err.value)
    assert error_message == "Order not found. Please ensure you have confirmed your order."

def test_when_dishes_added_get_grand_total_returns_correct_amount():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    assert my_order.get_grand_total() == "£15.95"

def test_get_itemised_list_returns_order_as_string():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Oxtail", menu)
    assert my_order.get_itemised_list() == "Jerk Chicken £9.95\nMac and Cheese £6.00\nOxtail £12.50"

def test_when_order_confirmed_view_receipt_returns_formatted_receipt():
    menu = Menu()
    my_order = OrderMeal()
    my_order.add_dish("Jerk Chicken", menu)
    my_order.add_dish("Mac and Cheese", menu)
    my_order.add_dish("Oxtail", menu)
    my_order.confirm_order()
    my_order.get_itemised_list()
    my_order.get_grand_total()
    my_receipt = Receipt()
    assert my_receipt.view_receipt(my_order) == "Your order:\nJerk Chicken £9.95\nMac and Cheese £6.00\nOxtail £12.50\n \nGrand Total: £28.45"