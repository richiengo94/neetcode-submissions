class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []

        open_paren: list = ["(", "{", "["]
        closed_paren: dict = {"]": "[", "}": "{", ")": "("}

        if len(s) % 2:
            return False

        for i in s:
            if i in open_paren:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() != closed_paren[i]:
                        return False

        return len(stack) == 0