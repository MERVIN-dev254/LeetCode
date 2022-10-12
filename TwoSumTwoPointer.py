#Two pointer technique..used for search. It uses 2 pointers in one loop over the given data structure
#Used for problems related to strings, arrays and linked lists.
#depending on whether the DS is sorted or not it can take O(n log n) or O(n)
#Variants - Opposite directional, Unidirectional
#Opposite directional problems - Two Sum II, Valid Palindrome, Reverse String
#Remove Element etc.

#Two sum problem Soln - Using unidircetional two pointer technique

def twoSum(List: nums, target: int) -> result:List:
	start = 0
	end = len(nums) - 1
	result = []

	while start < end:
		sum = nums(start) + nums(end)
		if sum == target:
			result[0] = start + 1
			result[1] = end + 1
			break
		else if sum < target:
			start ++
		else:
			end --
		
	return result

#Max sum of k elements in an array
#input (a list of integers, window size integer k)
#output ==> Maximum sum of k elements in the list
#Solving this using the sliding window technique
#Can be viewed as equi-directional two pointer technique 

def maxWindowSum(nums: List, k: int) --> maxSum: int:
	start, end, maxSum, winSum = 0, 0, 0, 0
	end += k - 1

	while end < len(nums):
		currSum = sum(nums[start:end])
		
		if currSum > maxSum:
			maxSum = currSum
		start +=1
		end += 1

	return maxSum

		 
