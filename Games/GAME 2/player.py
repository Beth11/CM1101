from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
mass = items["laptop"]["mass"] + items["money"]["mass"] + items["id"]["mass"]
max_weight = 6

# Start game at the reception
current_room = rooms["Reception"]
