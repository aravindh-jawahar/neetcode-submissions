class Solution:
    def isValid(self, s: str) -> bool:
        isValid = True

        mapped_pairs = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
        }

        stack = []

        for index, char in enumerate(s):
            if char in mapped_pairs:
                stack.append(char)
            else:
                if not stack or char != mapped_pairs[stack.pop()]:
                    return False 

        return len(stack) == 0 
        