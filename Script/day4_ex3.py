#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db import HomeDB
from db import haversine as get_distance
from db import plot

lat =   59.865795990339876
lon =   17.64583576202392
radius  =   2000

# Initilizing the database
database = HomeDB('uppsala.sqlite')
database.connect()
selection = database.select('rooms > 1 and rooms < 3 and area > 58 and rent < 3000')
database.disconnect()
print (selection)

# Looping now through the selections

# selected_home = []
for home in selection:
    if home in HomeDB:
#    selected = get_distance(lat,lon, home[10], home[11])

#     if distance < radius:
#         selected_home = home
#
#
#
#
#
# # Then plot