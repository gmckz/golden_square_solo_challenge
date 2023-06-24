from datetime import datetime

class OrderMeal:
    def __init__(self):
        self.order = {}
        self.order_confirmed = False
        self.order_time = None
        self.grand_total = 0

    def add_dish(self, dish, menu_obj):
        if menu_obj.has_dish(dish) == False:
            raise Exception(f"{dish} is not on the menu.")
        else:
            self.order[dish] = menu_obj.view_menu()[dish]

    def confirm_order(self):
        if self.order == {}:
            raise Exception("Please add dishes to order before confirming.")
        else:
            self.order_confirmed = True
            self.order_time = datetime.now()

    def get_grand_total(self):
        if self.order == {}:
            return self.grand_total
        else:
            self.grand_total = sum(self.order.values())
        if str(self.grand_total)[-2] == ".":
            return f"£{self.grand_total}0"
        else:
            return f"£{self.grand_total}"

    def get_itemised_list(self):
        itemised_list = []
        for dish, price in self.order.items():
            if str(price)[-2] == ".":
                itemised_list.append(f'{dish} £{price}0')
            else:
                itemised_list.append(f'{dish} £{price}')
        return "\n".join(itemised_list)