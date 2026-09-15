class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        u=0
        v=1
        for i in range(n):
            if nums[i]%2==0:
                ans[u]=nums[i]
                u+=2
            else:
                ans[v]=nums[i]
                v+=2
        return ans
        
