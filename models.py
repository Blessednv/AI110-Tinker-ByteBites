class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_to_history(self, order):
        self.purchase_history.append(order)
    

class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_price(self):
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def compute_total(self):
        return sum(item.price for item in self.items)