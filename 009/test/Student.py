#!/usr/bin/env python3

from Human import Human

class Student(Human):
    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number
