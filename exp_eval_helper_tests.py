import unittest
from exp_eval import *


class test_helpers(unittest.TestCase):
    def test_type_check_00(self):
        self.assertEqual(type_check("1"), 0)
        self.assertEqual(type_check("-10"), 0)
        self.assertEqual(type_check("1.62890"), 0)
        self.assertEqual(type_check("4730"), 0)

    def test_type_check_01(self):
        self.assertEqual(type_check("+"), 1)
        self.assertEqual(type_check("-"), 1)

    def test_type_check_02(self):
        self.assertEqual(type_check("*"), 2)
        self.assertEqual(type_check("/"), 2)

    def test_type_check_03(self):
        self.assertEqual(type_check("**"), 3)

    def test_type_check_04(self):
        self.assertEqual(type_check("<<"), 4)
        self.assertEqual(type_check(">>"), 4)

    def test_type_check_05(self):
        self.assertEqual(type_check("("), 5)

    def test_type_check_06(self):
        self.assertEqual(type_check(")"), 6)

    def test_type_exception_01(self):
        try:
            type_check("a")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_type_exception_02(self):
        try:
            type_check("^")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_valid_except_01(self):
        try:
            postfix_valid("4 3 + 5 + + 6")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_valid_except_02(self):
        try:
            postfix_valid("1 2 + 3 + 3 5 + 4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_valid_except_03(self):
        try:
            postfix_valid("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_valid_except_04(self):
        try:
            postfix_valid("( 3 4 ) + ")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_valid_01(self):
        self.assertTrue(postfix_valid("3 4 +"))

    def test_postfix_valid_02(self):
        self.assertTrue(postfix_valid("3 4 ** 4 / 4 +"))

    def test_postfix_valid_03(self):
        self.assertTrue(postfix_valid("3 4 >>"))

if __name__ == "__main__":
    unittest.main()
