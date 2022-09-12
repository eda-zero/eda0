from node import *

def Not(a):
    return Node("not", [a])

def Nand(a,b):
    return Node("nand", [a,b])

def And(a,b):
    return Node("and", [a,b])

def Or(a,b):
    return Node("or", [a,b])

def Xor(a,b):
    return Node("xor", [a,b])
