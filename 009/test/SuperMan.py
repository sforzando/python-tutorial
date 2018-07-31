#!/usr/bin/env python3
from Human import Human

class SuperMan(Human):
    def __init__(self, number):
        self.__number = 9

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = 9
