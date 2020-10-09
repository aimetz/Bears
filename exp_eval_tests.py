# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)

    def test_postfix_eval_03(self):
        self.assertAlmostEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)

    def test_postfix_except_01(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_except_02(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_except_03(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_except_04(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_except_05(self):
        try:
            postfix_eval(infix_to_postfix("3 << ( 4 / 8 )"))
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_except_06(self):
        try:
            postfix_eval(infix_to_postfix("3 >> ( 4 / 8 )"))
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_except_07(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 4 ** 0 /")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("1 ** 2 ** 3"), "1 2 3 ** **")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("4.5 ** ( -3 + 4 / ( 2 - 1 ) * 8 ) / 1.4"), "4.5 -3 4 2 1 - / 8 * + ** 1.4 /")

    def test_combo_01(self):
        s = infix_to_postfix("3 * ( 4 << 1 ** 3 )")
        self.assertEqual(postfix_eval(s), 1536)

    def test_combo_02(self):
        s = infix_to_postfix("3 * ( 4 / ( 2 + 3 * 2 ) )")
        self.assertEqual(postfix_eval(s), 1.5)

    def test_combo_03(self):
        s = infix_to_postfix("2 ** ( 3 << 1 - 10 )")
        self.assertEqual(postfix_eval(s), .0625)

    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_02(self):
        self.assertEqual(prefix_to_postfix("* + 3 4 + 6 7"), "3 4 + 6 7 + *")

    def test_prefix_to_postfix_03(self):
        self.assertEqual(prefix_to_postfix("7"), "7")


if __name__ == "__main__":
    unittest.main()
