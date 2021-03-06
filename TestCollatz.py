#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "5 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  5)
        self.assertEqual(j, 20)

    def test_read_3(self):
        s = "88 91\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 88)
        self.assertEqual(j, 91)

    # ----
    # eval
    # ----

# Fix these methods, the assert equal is not correct for some
# FIXED

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(6, 15)
        self.assertEqual(v, 20)

    def test_eval_7(self):
        v = collatz_eval(1, 5)
        self.assertEqual(v, 8)

    def test_eval_8(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 6, 15, 20)
        self.assertEqual(w.getvalue(), "6 15 20\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 1, 5, 8)
        self.assertEqual(w.getvalue(), "1 5 8\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertEqual(w.getvalue(), "10 10 7\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("1 2\n57 66\n265 310\n7328 8372\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 2 2\n57 66 108\n265 310 123\n7328 8372 252\n")

    def test_solve_3(self):
        r = StringIO("96 31\n45 17\n35 35\n7 16\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "96 31 116\n45 17 112\n35 35 14\n7 16 20\n")

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
