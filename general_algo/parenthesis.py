def check_balanced_parenthesis(expression):
    """
    Given an expression (string) such that it contains three 
    types of parenthesis: (), {}, []
    Check if the expression has balanced parenthesis

    e.g.:
    "{(A + B) + (C + D)}" should return True
    "{(x + y) * (z)" should return False
    ")(" should return False
    """
    # two main properties are conserved:
    # 1. number of opening parenthesis = number of closing parenthesis
    # 2. last unclosed parenthesis should be the first to close

    # use a stack to keep track opening parenthesis
    # when encounter a closing parenthesis,
    # check the last opening parenthesis is a valid pair

    # run time: O(N)
    # space: O(N)
    stack = []
    paired = {")": "(", "}": "{", "]": "["}
    for i in range(len(expression)):
        if expression[i] in "({[":
            stack.append(expression[i])
        elif expression[i] in ")}]":
            if len(stack) == 0:
                return False
            last_unclosed = stack.pop(-1)
            if paired[expression[i]] != last_unclosed:
                return False
    # valid if empty stack
    return len(stack) == 0


def test():
    inputs = ["{(A + B) + (C + D)}", "{(x + y) * (z)", ")(", "[(])", "{a + z)"]
    expected = [True, False, False, False, False]
    for i in range(len(inputs)):
        actual = check_balanced_parenthesis(inputs[i])
        assert actual == expected[i]


test()
