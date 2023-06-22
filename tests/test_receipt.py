from lib.receipt import *
from unittest.mock import Mock
import pytest

def test_contructs_order():
    my_order = Mock()
    my_receipt = Receipt(my_order)
    assert my_receipt.order == my_order

def test_when_order_not_confirmed_view_receipt_raises_error():
    my_order = Mock()
    my_order.confirm_order.return_value = False
    my_receipt = Receipt(my_order)
    with pytest.raises(Exception) as err:
        my_receipt.view_receipt()
    error_message = str(err.value)
    assert error_message == "Order not found. Please ensure you have confirmed your order."
