# Veneer - Buying and selling art

class Artt:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return f'{self.artist}. "{self.title}". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}.'

class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listings(self, new_listing):
    return self.listings.append(new_listing)

  def remove_listings(self, listing_to_delete):
    return self.listings.remove(listing_to_delete)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listings(new_listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listings(art_listing)    

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return f'{self.art}, {self.price}'

veneer = Marketplace()
edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
veneer.show_listings()
