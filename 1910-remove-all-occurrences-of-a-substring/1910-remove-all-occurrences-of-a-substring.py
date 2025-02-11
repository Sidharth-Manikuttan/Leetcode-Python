class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        M=len(part)
        for c in s:
            stack.append(c)
            if len(stack)>=M:
                if "".join(stack[-M:])==part:
                    for _ in range(M):
                        stack.pop()
        return "".join(stack)
        


        