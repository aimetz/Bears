from stacks import *


def type_check(character):
    if ord("0") <= ord(character) <= ord("9"):
        return 0
    elif character in ["+", "-"]:
        return 1
    elif character in ["*", "/"]:
        return 2
    elif character in ["^"]:
        return 3
    elif character in ["("]:
        return 4
    elif character in [")"]:
        return 5
    else:
        raise ValueError


def infix_to_postfix(input_str):
    operators = StackArray(30)
    postfix = ""
    i = 0
    while i < len(input_str):
        type = type_check(input_str[i])
        if len(postfix) > i:
            i = len(postfix)
        if type == 4:
            new = infix_to_postfix(input_str[i + 1:len(input_str)])
            postfix += new
            i += len(new) + 2
        elif type == 5:
            while not operators.is_empty():
                postfix += operators.pop()
            return postfix
        elif type == 0:
            postfix += input_str[i]
            i += 1
        elif type in [1, 2, 3]:
            if operators.is_empty():
                operators.push(input_str[i])
                i += 1
            else:
                if type_check(operators.peek()) >= type and not operators.is_empty():
                    postfix += operators.pop()
                    operators.push(input_str[i])
                    i += 1
                else:
                    operators.push(input_str[i])
                    i += 1
        else:
            i += 1
    while not operators.is_empty():
        postfix += operators.pop()
    return postfix


print(infix_to_postfix("3+4^(5+3)*(4+2)"))
print(infix_to_postfix("3+4^((5+3)*(4+2))"))