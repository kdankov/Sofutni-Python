class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        
    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'
    
    def get_capacity(self):
        return self.__capacity
    
    def __repr__(self):
        return 'Items: {0}.\nCapacity left: {1}'.format(', '.join(self.items), len(self.items) - self.__capacity) 
        
inventory = Inventory(2)
inventory.add_item("potion") 
inventory.add_item("sword") 
print(inventory.add_item("bottle")) 
print(inventory.get_capacity())
print(inventory)