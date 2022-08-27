import json

class vehicle:
    def init(self,name,engine,price):
        self.name=name
        self.engine=engine
        self.price=price
vehicle=vehicle("toyota rav4","2.5l",32000)
a=json.dumps(vehicle)
print(a)



