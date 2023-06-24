class Receipt:

    def __init__(self):
        pass

    def view_receipt(self, order_obj):
        if order_obj.order_confirmed == False:
            raise Exception("Order not found. Please ensure you have confirmed your order.")
        else:
            return f"Your order:\n{order_obj.get_itemised_list()}\n \nGrand Total: {order_obj.get_grand_total()}"
