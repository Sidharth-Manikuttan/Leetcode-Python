class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
       c=collections.Counter()
       ans=[]
       for x,y in zip(A,B):
        c[x]+=1
        c[y]+=1
        ans.append(sum(1 for x in c.keys() if c[x]==2))
       return ans
