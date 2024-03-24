def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 5):
	    ret_values.append(1)
	else:
	    n_str = str(n)
	    nums = list(n_str)
	    nums[0] = str((int(nums[0]) + 1))
	    for i in range(1, len(nums)):
	        nums[i] = '0'
	    n_str = ''
	    for i in nums:
	        n_str += i
	    ret_values.append((int(n_str) - n))

	return ret_values
