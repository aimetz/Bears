from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


# Assigns operators and operands integer values to help with precedence
# Handles Invalid Token Exception
# Str --> Int
def type_check(character):
    if character in ["+", "-"]:
        return 1
    elif character in ["*", "/"]:
        return 2
    elif character == "**":
        return 3
    elif character in ["<<", ">>"]:
        return 4
    elif character == "(":
        return 5
    elif character == ")":
        return 6
    else:
        try:
            float(character)
            return 0
        except ValueError:
            raise PostfixFormatException("Invalid token")


# Checks for correct number of tokens in Postfix expression
# Str --> Bool
def postfix_valid(input_str):
    numbers = Stack(30)
    ops = Stack(30)
    if input_str == "" or input_str == " ":
        raise PostfixFormatException("Empty input")
    input_list = input_str.split(" ")
    i = 0
    while i < len(input_list) and (numbers.num_items >= ops.num_items + 1 or numbers.num_items == ops.num_items == 0):
        type = type_check(input_list[i])
        if type == 0:
            numbers.push(input_list[i])
        elif 1 <= type <= 4:
            ops.push(input_list[i])
        else:
            raise PostfixFormatException("Invalid token")
        i += 1
    if numbers.num_items == ops.num_items + 1:
        return True
    elif numbers.num_items > ops.num_items + 1:
        raise PostfixFormatException("Too many operands")
    else:
        raise PostfixFormatException("Insufficient operands")


# Converts Prefix expressions to postfix
# Str --> Int/Float
def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    if postfix_valid(input_str):
        numbers = Stack(30)
        input_list = input_str.split(" ")
        i = 0
        while i < len(input_list):
            type = type_check(input_list[i])
            if type == 0:
                numbers.push(input_list[i])
            else:
                if input_list[i] == "+":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    numbers.push(a + b)
                elif input_list[i] == "-":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    numbers.push(b - a)
                elif input_list[i] == "*":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    numbers.push(a * b)
                elif input_list[i] == "/":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    if a == 0:
                        raise ValueError
                    numbers.push(b / a)
                elif input_list[i] == "**":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    numbers.push(b ** a)
                elif input_list[i] == "<<":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    if a == int(a) and b == int(b):
                        numbers.push(int(b) << int(a))
                    else:
                        raise PostfixFormatException("Illegal bit shift operand")
                elif input_list[i] == ">>":
                    a = float(numbers.pop())
                    b = float(numbers.pop())
                    if a == int(a) and b == int(b):
                        numbers.push(int(b) >> int(a))
                    else:
                        raise PostfixFormatException("Illegal bit shift operand")
            i += 1
        if int(numbers.peek()) == float(numbers.peek()):
            return int(numbers.pop())
        return numbers.pop()


# Converts Infix expressions to postfix
# Str --> Str
def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression
    Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    operators = Stack(30)
    input_list = input_str.split(" ")
    postfix = ""
    for i in range(len(input_list)):
        type = type_check(input_list[i])
        if type == 5:
            operators.push(input_list[i])
        elif type == 6:
            while not operators.is_empty() and operators.peek() != "(":
                postfix += operators.pop() + " "
            operators.pop()
        elif type == 0:
            postfix += input_list[i] + " "
        else:
            if operators.is_empty():
                operators.push(input_list[i])
            else:
                while not operators.is_empty() and (type <= type_check(operators.peek()) < 5
                                                    and not type == type_check(operators.peek()) == 3):
                        postfix += operators.pop() + " "
                operators.push(input_list[i])
    while not operators.is_empty():
        postfix += operators.pop() + " "
    return postfix[:len(postfix)-1]


# Converts Prefix expressions to postfix
# Str --> Str
def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    input_list = input_str.split(" ")
    nums = Stack(30)
    for i in range(1, len(input_list) + 1):
        type = type_check(input_list[len(input_list) - i])
        if type == 0:
            nums.push(input_list[len(input_list) - i])
        else:
            nums.push(nums.pop() + " " + nums.pop() + " " + input_list[len(input_list)-i])
    return nums.pop()

