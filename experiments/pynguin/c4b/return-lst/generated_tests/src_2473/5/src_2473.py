def func(*args):
	ret_values = []
	
	import sys
	f = sys.stdin
	nums = [int(x) for x in f.readline().rstrip().split()]
	poss = []
	poss.append(((nums[1] * nums[2]) // nums[6]))
	poss.append((nums[5] // nums[7]))
	poss.append((nums[3] * nums[4]))
	ret_values.append((min(poss) // nums[0]))

	return ret_values
