class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        for c in s:
            if c in [')', ']', '}']: 
                if len(stack) == 0:
                    return False
                else:
                    bracket = stack.pop()
                    if c == ')' and bracket != '(':
                        return False
                    elif c == '}' and bracket != '{':
                        return False
                    elif c == ']' and bracket != '[':
                        return False

            if c in ['(', '{', '[']:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False