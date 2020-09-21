from stacks import *


def type_check(character):
    if ord("0") <= ord(character) <= ord("9"):
        return 0
    elif character in ["+", "-"]:
        return 1
    elif character in ["*", "/"]:
        return 2
    elif character == "^":
        return 3
    elif character == "(":
        return 4
    elif character == ")":
        return 5
    else:
        raise ValueError


def infix_to_postfix(input_str):
    operators = StackArray(30)
    postfix = ""
    i = 0
    while i < len(input_str):
        type = type_check(input_str[i])
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
                if type_check(operators.peek()) >= type:
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


def postfix_eval(input_str):
    numbers = StackArray(30)
    answer = 0
    i = 0
    while i < len(input_str):
        type = type_check(input_str[i])
        if type == 0:
            numbers.push(input_str[i])
        else:
            if input_str[i] == "+":
                a = int(numbers.pop())
                b = int(numbers.pop())
                answer = a + b
                numbers.push(answer)
            elif input_str[i] == "-":
                a = int(numbers.pop())
                b = int(numbers.pop())
                answer = b - a
                numbers.push(answer)
            elif input_str[i] == "*":
                a = int(numbers.pop())
                b = int(numbers.pop())
                answer = a * b
                numbers.push(answer)
            elif input_str[i] == "/":
                a = int(numbers.pop())
                b = int(numbers.pop())
                answer = b / a
                numbers.push(answer)
            elif input_str[i] == "^":
                a = int(numbers.pop())
                b = int(numbers.pop())
                answer = b ** a
                numbers.push(answer)
        i += 1
    return answer

print(postfix_eval(infix_to_postfix("4^(1+1)*2+3")))


