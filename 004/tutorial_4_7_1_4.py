#!/usr/bin/env python3

def f(a, L=None): #fにはaとL=Noneの引数が入っている
    if L is None: #もしLがNoneであれば
        L = [] #Lはリスト化する
    L.append(a) #Lの[]にaを入れる
    return L #Lの値を返す

print(f(1)) #f(L[1])
print(f(2))
print(f(3))
