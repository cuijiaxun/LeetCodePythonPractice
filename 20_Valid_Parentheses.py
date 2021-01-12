class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(","{","["]:
                stack.append(c)
            else:
                if len(stack) == 0: return False
                top = stack.pop()
                if (c == ")" and top !="(") or\
                    (c == "}" and top !="{") or \
                    (c == "]" and top != "["):
                    return False
        if len(stack)>0: return False
        return True
