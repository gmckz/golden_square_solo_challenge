class Menu:
    
    def __init__(self):
        self.menu = {
            "Jerk Chicken": 9.95,
            "Oxtail": 12.50,
            "Mac and Cheese": 6.00,
            "Rice and Peas": 5.00
        }
    
    def view_menu(self):
        return self.menu
    
    def has_dish(self, dish):
        return dish in self.menu.keys()