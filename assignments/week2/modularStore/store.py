class Store:
    new_item = []
    def __init__(self,name):
        self.name = "Tienda"
        self.shirt = "shirt"
        self.pants = "pants"
        self.shorts = "shorts"
        self.skirt = "skirt"
        self.blouse = "blouse"
        self.run_shoes = "run_shoes"
        self.flats = "flats"
        self.heels = "heels"
        self.product = []
        self.price = 0.00
        
    def add_product(self,new_product):
        self.product.append(new_product)
        return self.product
        
    def sell_product(self, id):
        id = ["shirt", "pants", "shorts", "skirt", "blouse", "running shoes", "flats", "heels"]
        id[0], id[1] = "shirt","pants"
        id[2], id[3] = "shorts", "skirt"
        id[4], id[5] = "blouse", "running shoes"
        id[6], id[7] = "flats", "heels"
        for num in id:
            if len(self.product) > 0:
                self.product.pop()
        return self.product
    
    def inflation(self, percent_increase):
        self.price = (self.price * percent_increase) + self.price
        return self.price
    
    def set_clearance(self,category, percent_discount):
        self.price = (1- percent_discount) * self.price
        return self.price

class Product(Store):
    
    def __init__(self, name="Tienda",category="tops", price=0.00):
        super().__init__(name)
        self.name = name
        self.price = price
        self.category = ["tops", "bottoms", "shoes"]
        self.category[2] = self.run_shoes, self.flats, self.heels
        self.category[0] = self.shirt, self.blouse
        self.category[1] = self.pants, self.shorts, self.skirt
        self.store = Store(name)
       
    # update the price when a percent_change is passed in
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= (1 + percent_change)
        elif is_increased == False:
            price = price - (price * percent_change)
        return self
    
    def print_info(self):
        print(f" {self.name}: {self.price}")
        return self
    
    # method to set clearance on all items
    def clearance(self):
        self.store.set_clearance(category, percent_discount)
        return self
    
    #method to update all prices during times of inflation
    def inflated(self):
        self.store.inflation(percent_increase)
        return self
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.price}"   
    



