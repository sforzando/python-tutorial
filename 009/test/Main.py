#!/usr/bin/env python3

from Teacher import Teacher
from Student import Student

class Main():
    def __init__(self):
        self.t = Teacher(3)
        self.s = Student(5)
        

    def get_number(self):
        print('Teacher: {}'.format(self.t.get_number()))
        print('Student: {}'.format(self.s.get_number()))

    def set_student_number(self):
        self.t.number = 2
        # self.s.set_number(9)

if __name__ == '__main__':
    main = Main()
    main.get_number()
    main.set_student_number()
    main.get_number()
