class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{":"}","(":")","[":"]"}
        stack = []
        for i in s:
            if len(stack) > 0 and stack[-1] in pairs and pairs[stack[-1]]==i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
             