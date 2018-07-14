#!/usr/bin/env python3
import Student
import Teacher
import Human

class Main():
    def __init__(self):
        self.t = Teacher.Teacher(3)
        self.s = Student.Student(5)

    def get():
        print(t.get())
        print(s.get())

    def set():
        s.set(9)

if __name__ == "__main__":
    main = Main()
    main.get()
    main.set()
    main.get()
