"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x, y):
    return x*y

def id(x):
    return x

def add(x, y):
    return x+y

def neg(x):
    return -x

def lt(x, y):
    return x < y

def eq(x, y):
    return x == y

def max(x, y):
    return x if x>y else y

def abs(x):
    return x if x >= 0 else -x

def is_close(x, y):
    return abs(x-y) < 1e-2 

def sigmoid(x):
    return 1/(1+math.exp(-x))

def relu(x):
    return x if x>0 else 0

def log(x):
    return math.log(x)

def inv(x):
    return 1/x

def log_back(x, y):
    return 1/x * y

def inv_back(x, y):
    return -1/(x*x) * y

def relu_back(x, y):
    return y if x>0 else 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(fn, x_list):
    return [fn(x) for x in x_list]

def zipWith(x_list, y_list):
    res = []
    for i in range(len(x_list)):
        res.append([x_list[i], y_list[i]])
    return res

def reduce(fn, x_list):
    res = None
    for x in x_list:
        if res is None:
            res = x
        else:
            res = fn(res, x)
    return 0 if res is None else res

# TODO: Implement for Task 0.3.
def addLists(x_list, y_list):
    return [reduce(add, t) for t in zipWith(x_list, y_list)]

def negList(x_list):
    return map(neg, x_list)

def sum(x_list):
    return reduce(add, x_list)

def prod(x_list):
    return reduce(mul, x_list)

if __name__ == "__main__":
    print(sum([1,2,4,5.3]))
    print(prod([1,1.002,1]))