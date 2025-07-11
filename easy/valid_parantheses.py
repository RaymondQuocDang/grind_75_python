s = "()[]{}"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = { 
            ")": "(", 
            "]": "[",
            "}": "{"
        }
        
        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
    

sol = Solution()
response = sol.isValid(s)
print(response)