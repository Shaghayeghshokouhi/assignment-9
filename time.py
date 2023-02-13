# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 00:06:44 2023

@author: 2022
"""

class Time():
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        
    def show(self):
        print(self.h, ":", self.m, ":", self.s)
        
    def secondtotime(self):
        result = Time(None, None, None)
        result.h = self.s // 3600
        return result

    def timetosecond(self):
        result = Time(None, None, None)
        result.s = self.h * 60 * 60
        return result
    
    
time1 = Time(3, 47, 43)
time1.show()
time1.timetosecond()


s = 74637
print("second to hour")
result = secondtotime()
result.show()





        