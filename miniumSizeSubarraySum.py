def findMinSum(s, target):

	min_length = len(s) + 1

	start = 0
	end = 0
	curr_sum = 0
	while end < len(s):
		curr_sum += s[end]
		while curr_sum >= target:
			min_length = min(end - start + 1, min_length)
			curr_sum -= s[start]
			start += 1
		end += 1
	return min_length if min_length != len(s) + 1 else 0



print(findMinSum([2, 3, 1, 2, 4, 3], 7))
print(findMinSum([1, 4, 4], 4))
print(findMinSum([1, 1, 1, 1], 7))