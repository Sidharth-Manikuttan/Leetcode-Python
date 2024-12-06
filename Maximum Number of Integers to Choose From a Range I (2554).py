class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        count = 0
        current_sum = 0
        for num in range(1, n + 1):
            if num in banned_set:
                continue
            if current_sum + num <= maxSum:
                current_sum += num
                count += 1
            else:
                break
        return count
