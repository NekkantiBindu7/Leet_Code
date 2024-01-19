class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        zero,one,two=0,0,n-1
        while one<=two:
            if nums[one]==1:
                one+=1
            elif nums[one]==2:
                nums[one],nums[two]=nums[two],nums[one]
                two-=1
            else:
                nums[zero],nums[one]=nums[one],nums[zero]
                zero+=1
                one+=1