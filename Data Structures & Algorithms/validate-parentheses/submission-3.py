class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: return False
        stack = []
        for i in s:
            if i == "}" and len(stack)>0 and stack[-1]=="{":
                stack.pop()
            elif i == "]" and len(stack)>0 and stack[-1]=="[":
                stack.pop()
            elif i == ")" and len(stack)>0 and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)
        return not len(stack)
            