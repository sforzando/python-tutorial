#!/usr/bin/env python3
from Human import Human

class SuperMan(Human):
    def __init__(self, number):
        super().__init__(number = 9)
        
    def set_number(self, number):
        pass
