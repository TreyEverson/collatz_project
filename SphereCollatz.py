#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

# 10, 1 and 1, 1 are corner tests

import sys


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# ------------


cache = [0 for y in range(1000000)]  # manually setting the size of list and filling with 0's


def collatz_eval(i, j):
    # cache = [0 for y in range (1000000)]
    global cache    # using global variable proved to be much faster
    assert i > 0 and j > 0

    cache[1] = 1

    max_cycle = 0
    c = 0

    if i > j:   # if i > j, swap i and j
        temp = i
        i = j
        j = temp

    if i < j // 2:  # if i < j // 2 then there is no reason to calculate other numbers in the rage
        i = j // 2

    for x in range(i, j+1):
        c = 0
        if cache[x] != 0:   # if cache has the cycle length of x
            c = cache[x]
        else:   # if x is not in the cache
            spot = x    # saving origional spot for cache
            while x > 1:
                if x % 2 == 0:
                    x = x // 2
                    c += 1
                    # print(x)
                else:
                    # x = int((1.5 * x) + 0.5)
                    # bitwise shift proved to be faster than any other implementation
                    x = x + (x >> 1) + 1
                    c += 2
                    # print(x)
                if x < 1000000 and cache[x] != 0:
                    c += cache[x]   # can add because cache will be = 0
                    break
            x = spot   # saved origional cache spot
            cache[x] = c

        if max_cycle < c:
            max_cycle = c

    assert max_cycle > 0
    return max_cycle


# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        if not s.strip():
            continue
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


# ----
# main
# ----


if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
