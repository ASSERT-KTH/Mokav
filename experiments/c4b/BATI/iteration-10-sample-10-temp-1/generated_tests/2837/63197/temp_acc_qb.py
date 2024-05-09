def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n < 5):
	    global_list.append(1)
	else:
	    n_str = str(n)
	    nums = list(n_str)
	    nums[0] = str((int(nums[0]) + 1))
	    for i in range(1, len(nums)):
	        nums[i] = '0'
	    n_str = ''
	    for i in nums:
	        n_str += i
	    global_list.append((int(n_str) - n))
	return global_list