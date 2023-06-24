from lib.receipt import *
from unittest.mock import Mock
import pytest

# def test_when_order_confirmed_grand_total_returned():
#     my_order = Mock()
#     my_order.order = {"Jerk Chicken": 9.95, "Mac and Cheese": 6.00, "Rice and Peas": 5.00}
#     my_order.confirm_order.return_value = True
#     receipt = Receipt(my_order)
#     assert receipt.grand_total() == 18.95

def test_when_order_not_confirmed_view_receipt_raises_error():
    my_order = Mock()
    my_order.order_confirmed = False
    my_receipt = Receipt()
    with pytest.raises(Exception) as err:
        my_receipt.view_receipt(my_order)
    error_message = str(err.value)
    assert error_message == "Order not found. Please ensure you have confirmed your order."

def test_when_order_confirmed_view_receipt_returns_formatted_receipt():
    my_order = Mock()
    my_order.order_confirmed = True
    my_order.get_itemised_list.return_value = "Jerk Chicken £9.95\nMac and Cheese £6.00\nOxtail £12.50"
    my_order.get_grand_total.return_value = "£28.45"
    my_receipt = Receipt()
    assert my_receipt.view_receipt(my_order) == "Your order:\nJerk Chicken £9.95\nMac and Cheese £6.00\nOxtail £12.50\n \nGrand Total: £28.45"