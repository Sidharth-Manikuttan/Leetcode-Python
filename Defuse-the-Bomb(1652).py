class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        prefix = [0] * (2 * n)
        prefix[0] = code[0]
        for i in range(1, 2 * n):
            prefix[i] = prefix[i - 1] + code[i % n]

        res = [0] * n
        self.calculate_sum(res, k, prefix)
        return res
        
    def calculate_sum(self, res, k, prefix):
        n = len(res)
        if k > 0:
            for i in range(n):
                res[i] = prefix[i + k] - prefix[i]
        else:
            k = abs(k)
            for i in range(n, 2 * n):
                res[i - n] = prefix[i - 1] - prefix[i - k - 1]
