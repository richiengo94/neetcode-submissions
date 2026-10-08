class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result: int = 0
        stack: list[int] = []

        operators: list[str] = ["+", "-", "*", "/"]

        if len(tokens) == 1 and tokens[0] not in operators:
            return int(tokens[0])

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                operand2: int = stack.pop()
                operand1: int = stack.pop()
                if i == "+":
                    stack.append(operand1 + operand2)
                elif i == "-":
                    stack.append(operand1 - operand2)
                elif i == "*":
                    stack.append(operand1 * operand2)
                elif i == "/":
                    stack.append(int(operand1 / operand2))

        return stack[0]