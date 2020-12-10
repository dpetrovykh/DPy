#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:32:54 2020

@author: dpetrovykh
"""
import numpy as np

class Table_A_17:
    # Recreates Table A_17 of Shigley's Mechanical Engineering Design.
    def __init__(self):
        self.data = {}
        self.data["inch_frac"] = np.concatenate((np.array([1/64, 1/32, 1/16, 3/32, 1/8, 5/32, 3/16, 1/4, 5/16, 3/8, 7/16, 1/2, 9/16, 5/8, 11/16, 3/4, 7/8]), np.arange(1,6,0.25), np.arange(6,20.5,0.5)))
        self.data["inch_dec"] = np.concatenate((np.array([0.010, 0.012, 0.016, 0.020, 0.025, 0.032, 0.040, 0.050, 0.060, 0.080, 0.10,0.12, 0.16, 0.20, 0.24, 0.30, 0.40, 0.50]), np.arange(0.60,6.0,0.2), np.array([6.0, 7.0, 7.5]), np.arange(8.5, 20.5, 0.50) ))
        self.data["mm"] = np.concatenate((np.array([0.05, 0.06, 0.08, 0.10, 0.12, 0.16, 0.20, 0.25]), np.arange(0.30, 1.3, .1), np.array([1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 2.8]), np.arange(3.0, 7.0, 0.5), np.arange(7, 12, 1), np.arange(12, 24, 2), np.array([25,28,30,32,35,40,45,50,60,80,100,120,140,160,180,200,250,300])))
        self.acceptable_units = list(self.data.keys())
        
    def nearest_greater(self, exact, units = "inch_frac"):
        #returns an approximation for an exact value from a table
        # The approximation will be smallest value which is greater than or equal to the exact value.
        self.check_inputs(exact, units)
        data = self.data[units]
        for approx in data:
            if approx >= exact:
                return approx
        raise ValueError("Value for 'exact' larger than any in chosen unit list")
    
    def nearest(self, exact, units = "inch_frac"):
        #returns the nearest approximate value in the chosen table for the provided exact value
        self.check_inputs(exact, units)
        data = self.data[units]
        return data[min(range(len(data)), key = lambda i: abs(data[i]-exact))]
    
    def nearest_lesser(self, exact, units = "inch_frac"):
        #returns an approximation for an exact value from a table
        # The approximation will be largest value which is less than or equal to the exact value.
        self.check_inputs(exact, units)
        data = self.data[units]
        for index, approx in enumerate(data):
            if approx == exact:
                return approx
            elif approx > exact:
                return data[index-1]
    
    def check_inputs(self, exact, units):
        if units not in self.acceptable_units:
            raise ValueError(f"Please enter a value for units which is one of: {self.acceptable_units}")
        if exact<0:
            raise ValueError(f"Please enter a positive value for exact= {exact}")
        max_exact = max(self.data[units])
        if exact> max_exact:
            raise ValueError(f"Value of exact= {exact} larger than maximum of {max_exact} acceptable for unit choice of '{units}' .")
    
    
    
    
    
    # if __name__ == "__main__":
    #     tble = Table_A_17()
    #     tble(100)
    #     tble(-5)
    #     tble(1, units = "asdd")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    