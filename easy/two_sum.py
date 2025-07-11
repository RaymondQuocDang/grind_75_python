nums = [2,7,11,15]
target = 9


class Solution:
    def twoSum(self, nums, target) -> list[int]:
        result = []
        
        for i in range(len(nums) - 1):
            if nums[i] + nums[i+1] == target:
                result.append(i)
                result.append(i+1)
                break

        return result

sol = Solution()
result = sol.twoSum(nums, target)
print(result)