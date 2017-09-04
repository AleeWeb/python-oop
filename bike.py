

#class Bike variables attributes price, max_speed, miles
class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

#create 3 instances (objects from the Bike Class)

redBike = Bike("20", "9.6 mph","50")
#print redBike.price
#print redBike.max_speed
#print redBike.miles

blueBike = Bike("30", "10 mph","60")
#print blueBike.price
#print blueBike.max_speed
#print blueBike.miles

spaceBike = Bike("100", "90 mph","1000")
#print spaceBike.price
#print spaceBike.max_speed
#print spaceBike.miles

'''
displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
'''

def displayInfo(self):
    print self.price, self.max_speed, self.miles
    return self

displayInfo()

#def ride():

#def reverse():

#chain methods eventually
redBike.displayInfo().ride().reverse()



