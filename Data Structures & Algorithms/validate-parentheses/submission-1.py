class Solution:
    def isValid(self, s: str) -> bool:
        valid_parentheses_maps = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in valid_parentheses_maps.values():
                stack.append(c)
            elif c in valid_parentheses_maps.keys():
                if len(stack) == 0 or valid_parentheses_maps[c] != stack[-1]:
                    return False
                stack.pop()

        if not stack:
            return True
        return False
            