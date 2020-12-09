#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:13 2020

@author: dpetrovykh
"""
import math

class Circle:
    def __init__(self, radius= 1):
        self.radius = float(radius)
    
    @classmethod
    def fromDiameter(cls, diameter):
        return cls(radius = diameter/2)
    
    @property
    def area(self):
        return math.pi*self.radius**2
    
    @property
    def perimeter(self):
        return math.pi*self.radius*2
    
    @property
    def diameter(self):
        return self.radius*2