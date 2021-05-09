class car:
    def __init__(self,year,model,brand):
        self.year = year
        self.model = model
        self.brand = brand
        self.odometer = 0

    def describ(self):
        info = f'制造年份:{self.year} 品牌:{self.brand} 型号:{self.model}'
        return info

    def read_odometer(self):
        info = f"这辆车已经行驶了{self.odometer}公里"
        return info

    def update_odometer(self,odometer):
        if odometer>self.odometer:
           self.odometer = odometer
        else:
            print('你不能这样操作')

class new_car(car):
    def __init__(self,year,model,brand):
        super().__init__(year,model,brand)
        self.battery = 100

    def describ_battery(self):
        print(f'这辆车有{self.battery}kwh电量')

    def describ(self):
        info = f'(重写了)制造年份:{self.year} 品牌:{self.brand} 型号:{self.model}'
        return info

new_car = new_car('2021','model 3','TESLA')
print(new_car.describ())
new_car.describ_battery()

mycar = car('2021','model 3','TESLA')
print(mycar.describ())
# mycar.odometer = 100
# mycar.update_odometer(10)
# mycar.update_odometer(1)
# print(mycar.read_odometer())
