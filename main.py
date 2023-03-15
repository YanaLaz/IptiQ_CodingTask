class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            print(f"Item {name} is already exists. Use update_item for updating")
        else:
            self.items[name] = {"quantity": quantity, "price": price}
            print(f"Item {name} successfully added")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Item {name} successfully removed")
        else:
            print(f"Item {name} was not found")

    def update_item(self, name, quantity=None, price=None):
        if name in self.items:
            if quantity:
                self.items[name]["quantity"] = quantity
            if price:
                self.items[name]["price"] = price
            print(f"Item {name} successfully updated")
        else:
            print(f"Item {name} was not found")

    def all_items(self):
        print('---The list of items---')
        for name, details in self.items.items():
            print(f"{name}: {details['quantity']} x {details['price']}€")

# Usage
inventory = Inventory()

inventory.add_item("Book", 10, 12)
inventory.add_item("Bicycle", 5, 200)
inventory.add_item("Blanket", 15, 30)
inventory.add_item("Pillow", 4, 40)
inventory.add_item("Book", 5, 10)  # Should print "Item {name} is already exists."

inventory.update_item("Book", quantity=10)
inventory.update_item("Blanket", price=28)

inventory.remove_item("Apple")  # Should print "Item not found"
inventory.remove_item("Bicycle")

inventory.all_items()
