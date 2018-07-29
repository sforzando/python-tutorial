#!/usr/bin/env python3

class Human(object):
    def __init__(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number
