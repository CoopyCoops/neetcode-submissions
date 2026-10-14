class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = 0
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                r = stack.pop()
                l = stack.pop()
                if token == "+":
                    res = int(l) + int(r)
                elif token == "-":
                    res = int(l) - int(r)
                elif token == "*":
                    res = int(l) * int(r)
                else:
                    res = int(int(l) / int(r))
                stack.append(res)
            else:
                stack.append(token)
        
        ans = stack.pop()
        return int(ans)