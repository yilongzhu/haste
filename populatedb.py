from app import db
from app.models import Item

items = [
    {"name": "apple", "price": 1.2},
    {"name": "banana", "price": 1.3},
    {"name": "orange", "price": 1.1},
    {"name": "shampoo", "price": 5.5},
    {"name": "towel", "price": 2.3},
    {"name": "peanut butter", "price": 4.99},
    {"name": "cup noodle", "price": 0.99},
    {"name": "laundry detergent", "price": 8.5},
    {"name": "water - 24 pack", "price": 9.99},
    {"name": "gatorade - 6 pack", "price": 8.5},
    {"name": "doritos", "price": 2.99},
    {"name": "granola bars", "price": 5},
    {"name": "notebook","price": 1.89},
    {"name": "pencil","price": 0.5},
    {"name": "pen","price": 0.89},
    {"name": "pillow","price": 8.67},
    {"name": "water boiler","price": 24.99},
    {"name": "lightbulb","price": 3.45},
    {"name": "bar of soap","price": 1.67},
    {"name": "toothpaste","price": 5.89},
    {"name": "toothbrush","price": 1.99},
    {"name": "socks","price": 2.99},
    {"name": "t-shirt","price": 9.99},
    {"name": "air freshener","price": 6.89},
    {"name": "shower basket","price": 5.35},
    {"name": "shower slippers","price": 6.99},
    {"name": "ramen - 6 pack","price": 5.99},
    {"name": "ramen - 24","price": 20.59},
    {"name": "lamp","price": 18.99},
    {"name": "milk - gallon","price": 4.99},
    {"name": "oatmeal","price": 8},
    {"name": "protein powder","price": 20},
    {"name": "gelato","price": 7.99},
    {"name": "Sprite - 24 cans","price": 5.99},
    {"name": "Coke - 24 cans","price": 5.99},
    {"name": "contact solution","price": 7},
    {"name": "conditioner","price": 6.5},
    {"name": "gum - 8 pack","price": 8},
    {"name": "Frosted Flakes","price": 3.99},
    {"name": "Cheerios","price": 3.99},
    {"name": "cereal bar","price": 6},
    {"name": "tissues - 3 boxes","price": 4},
    {"name": "iPhone charger","price": 8},
    {"name": "Cocoa Puffs","price": 5.99},
    {"name": "Vitamin Water","price": 2.99},
    {"name": "Redbull","price": 3.99},
    {"name": "bread loaf","price": 4.5},
    {"name": "frozen ham","price": 8.5},
    {"name": "Nutella","price": 5.99},
    {"name": "dryer sheets","price": 5.89},
    {"name": "Trojan condoms","price": 14.89},
    {"name": "Arizona Iced Tea","price": 2.89},
    {"name": "Oreos","price": 3.5},
    {"name": "hot sauce","price": 3.89}
]

for item in items:
    i = Item(name=item["name"], price=item["price"])
    db.session.add(i)

db.session.commit()