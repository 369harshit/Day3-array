from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        Pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    Pairs += 1
        return Pairs


if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.reversePairs([1, 3, 2, 3, 1])
    print("The total number of Reverse Pairs are", totalCount)