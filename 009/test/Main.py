#!/usr/bin/env python3

from Teacher import Teacher
from Student import Student

class Main():
    def __init__(self):
        self.t = Teacher(3)
        self.s = Student(5)

    def 出席を取ります(self):
        print('Teacher: {}'.format(self.t.get_number()))
        print('Student: {}'.format(self.s.get_number()))

    def 番号を変えます(self):
        self.s.set_number(9)

if __name__ == '__main__':
    main = Main()
    main.出席を取ります()
    main.番号を変えます()
    main.出席を取ります()
