class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N=len(pref)
        res=0
        for w in words:
            inc=1
            if len(w)<N:
                continue
            for i in range(N):
                if w[i]!=pref[i]:
                    inc=0
                    break
            res+=inc
        return res

        