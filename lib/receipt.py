class Receipt:

    def __init__(self, order_obj):
        self.order = order_obj

    def view_receipt(self):
        raise Exception("Order not found. Please ensure you have confirmed your order.")
