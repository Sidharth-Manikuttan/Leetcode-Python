class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ev=[]
        for s,e,v in events:
            ev.append((s,1,v))
            ev.append((e+1,-1,v))
        ev.sort()
        maxp=0
        best=0
        for x, t, v in ev:
            if t==1:
                best=max(best,maxp+v)
            if t==-1:
                maxp=max(maxp,v)
        return best
