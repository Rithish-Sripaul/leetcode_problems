def sortColors(nums):
	low = 0
	right = len(nums) - 1
	for i in range(len(nums)):
		if nums[i] == 0:
			nums[i], nums[low] = nums[low], nums[i]
			low += 1
		elif nums[i] == 2:
			nums[i], nums[right] = nums[right], nums[i]
			right -= 1
	print(nums)

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
