1. Describe the problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.
-use twilio-python package to implement
-use mocks for testing
-think about security implications of pushing twilio api key to a public github repo... How will you keep that information out of your repo?

2. Design the class system



class Menu:
    #user-facing properties:
    # menu: a dictionary of dishes as keys and prices as values

    def __init__(self):
        pass

    def view_menu(self):
        #Parameters:
        # none
        #Returns:
        # the dictonary of menu items and prices
        #Side-effects:
        # none
        pass


class OrderMeal:
    #user-facing properties:
    #  order: a dictionary of selected dishes as keys and their prices as values

    def __init__(self):
        pass

    def add_dish(dish, menu):
        #Parameters:
        #  dish: a string, naming a dish from menu
        #  menu: an instance of Menu
        #Returns:
        #  nothing
        #Side-effects:
        #  updates the order dictionary 
        pass

    def confirm_order(self):
        #Parameters:
        #  none
        #Returns:
        #  confirmation text message 
        #Side-effects:
        #  sets order_confirmed to True
        #  sets order_time to current time
        pass

    def itemised_list():
        #Parameters:
        #  none
        #Returns:
        #  nothing
        #Side-effects:
        #  creates itemised list from orders
        pass

    def grand_total():
        #Parameters:
        #  none
        #Returns:
        #  nothing
        #Side-effects:
        #  creates grand total variable 
        pass

class Receipt:
    #user-facing properties:
    #  none

    def __init__(self, order_obj):
        pass

    def view_receipt(self):
        #Parameters:
        #  none
        #Returns:
        #  an itemised list and grand total as a string
        #side-effects:
        #  none
        pass

class ConfirmationText()
    #user-facing properties:
    #  none
    
    def __init__(self):
        pass

    def send_text(self, ?):
        #Parameters:
        #   ?
        #Returns:
        #  a text message "Thank you! Your order was placed and will 
        #  be delivered before {time}
        #Side-effects:
        #  sets delivery time to current time + 30 minutes
        pass

3. Create examples as integration tests

"""
Given a menu
When a dish that is not on the menu is added
#add_dish raises error
"""


"""
Given a menu
When three dishes from the menu are added to order
We see those dishes reflected in order dictionary
"""


"""
When order dictionary is empty
#confirm_order raises error
"""

"""
When order dictionary not empty
#confirm_order sets order_confirmed to True
and order_time to current time
"""

"""
When order dictionary not empty
#confirm_order returns text message with delivery time
"""

"""
When order has not been confirmed 
#view_receipt raises error
"""

"""
When order confirmed
#grand_total returns grand total cost of order
"""

"""
When order has been confirmed
#view_receipt returns receipt with itemised list and grand total
"""


4. Create examples as unit tests
#MENU
"""
#view menu returns the dictionary containing dishes and prices
"""
#ORDERMEAL
"""

"""


5. Implement the behaviour