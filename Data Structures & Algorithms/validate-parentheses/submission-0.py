class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in close_to_open:
                if len(stack) > 0:
                    top_element = stack[-1]
                else:
                    top_element = "awef"
                if top_element != close_to_open[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True
