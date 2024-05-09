def original_func(*args):
	global_list = []
	
	nums = args[0]
	nums = nums.split(' ')
	nums = list(map(int, nums))
	if (((nums[1] - nums[0]) % 2) == 0):
	    global_list.append('2')
	else:
	    global_list.append('3')
	return global_list