class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix=[0 for i in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        ans=[]
        for start,end in queries:
            ans.append(prefix[start]==prefix[end])
        return ans
