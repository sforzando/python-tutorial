#!/usr/bin/env python3

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# # --------------------

# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()

        
# # --------------------

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# # --------------------

# def f(a, L=None): #fにはaとL=Noneの引数が入っている
#     if L is None: #もしLがNoneであれば
#         L = [] #Lはリスト化する
#     L.append(a) #Lの[]にaを入れる
#     return L #Lの値を返す

# print(f(1)) #f(L[1])
# print(f(2))
# print(f(3))

# # --------------------
