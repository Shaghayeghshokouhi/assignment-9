# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:10:07 2023

@author: 2022
"""

class fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m
    def show(self):
        print(self.soorat, "/", self.makhraj)
        
    def sub(self, f):
        result = fraction(None, None)
        result.soorat = (self.soorat * f.makhraj) - (self.makhraj * f.soorat)
        return result
    def div(self, f):
        result = fraction(None, None)
        result.soorat = (self.soorat * f.makhraj)
        result.makhraj = (self.makhraj * f.soorat)
        return result
    
fraction1 = fraction(3,4)
fraction2 = fraction(5,7)

result_div = fraction1.div(fraction2)
result_sub = fraction1.sub(fraction2)

result_div.show()
result_sub.show()
        
              
        