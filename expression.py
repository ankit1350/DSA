class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0   # ✅ fixed

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def infixToPostfix(infixexpression):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opstack = Stack()
    postfixList = []
    tokenList = infixexpression.split()

    for token in tokenList:
        if token.isalnum():  # ✅ handles numbers and variables
            postfixList.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            topToken = opstack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:  # operator
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)


# Example Run
infix = input("Enter the infix expression to convert to postfix expression: ")
print("Postfix Expression:", infixToPostfix(infix))
