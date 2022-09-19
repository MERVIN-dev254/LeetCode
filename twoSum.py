class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(numbers):
            num = target - n
            if num in my_dict:
                return [my_dict[num] + 1, i + 1]
            my_dict[n] = i