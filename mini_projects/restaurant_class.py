#create menus
brunch_menu = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }

early_bird_menu = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
    }

dinner_menu = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
    }

kids_menu = {
        'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
        }

#create class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return(f"{self.name} menu available from {self.start_time} to {self.end_time}")

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

# Menu information
brunch = Menu("Brunch", brunch_menu, 1100, 1600)
early_bird = Menu("Early Bird", early_bird_menu, 1500, 1800)
dinner = Menu("Dinner", dinner_menu, 1700, 2300)
kids = Menu("Kids", kids_menu, 1100, 2100)

#print(f"{brunch}\n{early_bird}\n{dinner}\n{kids}\n")

# Brunch customer
brunch_meal = ['pancakes', 'home fries', 'coffee']
brunch_bill = brunch.calculate_bill(brunch_meal)
#print(f"Brunch bill is {brunch_bill}")

# Early Bird customer
early_bird_meal = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_bill = early_bird.calculate_bill(early_bird_meal)
#print(f"Early bird bill is {early_bird_bill}")

# Create menus
menus = [brunch, early_bird, dinner, kids]

# Create Franchise Class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return f"The address is: {self.address}"

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu) 
    return available_menus

flagship = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#print(flagship.available_menus(1700))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

franchises = [flagship, new_installment]

basta = Business("Basta Fazoolin' with my Heart", franchises)

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas = Menu("Arepas", arepas_menu, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas)
new_business = Business("Take a' Arepa", arepas_place)
# print(arepas)
# print(arepas_place)
print(new_business.franchises.menus)


