#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def dist(x1,x2,y1,y2):
    d = ((x2-x1)**2) + ((y2-y1)**2)
    return math.sqrt(d)

def calculte_angle(x1,x2,y1,y2):
    d = ((x2-x1)**2) + ((y2-y1)**2)
    a = math.acos((x2-x1)/d)
    return a

test1 = dist(2,5,8,10)
test2 = calculte_angle(2,5,8,10)
print (test1,test2)