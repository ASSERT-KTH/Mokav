def patched_func(*args):
	global_list = []
	
	nums = args[0]
	nums = nums.split(' ')
	nums = list(map(int, nums))
	if (nums[0] == nums[1]):
	    global_list.append(nums[0])
	elif (((nums[1] - nums[0]) % 2) == 0):
	    global_list.append('2')
	elif ((((nums[1] - nums[0]) % 2) == 1) and (((nums[0] % 2) == 0) or ((nums[1] % 2) == 0))):
	    global_list.append('2')
	else:
	    global_list.append('3')
	return global_list