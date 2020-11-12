#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


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


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # Instantiating the lazy cache as a dictionary
    lazy_cache = {}

    assert i > 0 and j > 0
    max_cycle = 1

    if i > j:   # if i > j, flip the two numbers
        temp = i
        i = j
        j = temp

    if i == j:  # if i and j are the same number we compute cycle length like this
        """
        if i in lazy_cache:
        assert lazy_cache[i] > 0
        return lazy_cache[i]
        else:
        """
        c = 1
        while i > 1:
            if (i % 2) == 0:
                i = (i // 2)
                c += 1
            else:
                i = (3 * i) + 1
                c += 1
        lazy_cache[i] = c
        assert c > 0
        return c

    for x in range(i, j+1):
        c = 1
        while x > 1:
            if x in lazy_cache:  # checking if x is in the cashe
                c = (lazy_cache[x]) + c - 1
                # print("CYCLE LENGTH FOR", i, " = ", c)
                x = 1
            else:   # if x is not in cache we compute normally
                if (x % 2) == 0:
                    x = (x // 2)
                    c += 1
                    # print("CYCLE LENGTH FOR", i, " = ", c)
                else:
                    x = (3 * x) + 1
                    c += 1
                    # print("CYCLE LENGTH FOR", i, " = ", c)
        if max_cycle < c:
            max_cycle = c
        lazy_cache[i] = c   # adding new cycle length to cache
        x += 1
        i += 1
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
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
