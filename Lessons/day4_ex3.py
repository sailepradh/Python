#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db import HomeDB
from db import HomeEntry
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


# Looping now through the selections


selected_home = []
cheapest_home = ''
#
for home in selection:
    (la1,lng1) = home.get_location()

    dist = get_distance(lat,lon,la1,lng1)

    if dist < radius:
        selected_home.append(home)

        if not cheapest_home:
            cheapest_home = home
        elif home.get_price()  <  cheapest_home.get_price():
            cheapest_home = home

plot(selected_home,
     output = 'selection.html',
     cheapest = cheapest_home,
     zoom = 14,
     latitude=lat,
     longitude=lon,
     radius=radius, # in m
     google_key = 'AIzaSyC_bDDqiXuZtYgGfkGZwuE-O_p2QyGqyJk'
)