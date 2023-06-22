from datetime import datetime

class OrderMeal:
    def __init__(self, menu_obj):
        self.order = {}
        self.menu_obj = menu_obj
        self.order_confirmed = False
        self.order_time = None

    def add_dish(self, dish):
        if dish not in self.menu_obj.menu:
            raise Exception(f"{dish} is not on the menu.")
        else:
            self.order[dish] = self.menu_obj.menu[dish]

    def confirm_order(self):
        if self.order == {}:
            raise Exception("Please add dishes to order before confirming.")
        else:
            self.order_confirmed = True
            self.order_time = datetime.now()