def func(*args):
	ret_values = []
	
	nums = args[0]
	nums = nums.split(' ')
	nums = list(map(int, nums))
	if (nums[0] == nums[1]):
	    ret_values.append(nums[0])
	elif (((nums[1] - nums[0]) % 2) == 0):
	    ret_values.append('2')
	elif ((((nums[1] - nums[0]) % 2) == 1) and (((nums[0] % 2) == 0) or ((nums[1] % 2) == 0))):
	    ret_values.append('2')
	else:
	    ret_values.append('3')

	return ret_values
