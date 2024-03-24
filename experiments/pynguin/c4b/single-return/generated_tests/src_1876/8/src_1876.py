def func(*args):
	
	import sys
	
	def generate_lucky_nums(cur_num=0):
	    if (cur_num > (10 ** 10)):
	        return
	    if (cur_num != 0):
	        lucky_nums.append(cur_num)
	    generate_lucky_nums(((cur_num * 10) + 4))
	    generate_lucky_nums(((cur_num * 10) + 7))
	
	def bin_search(target, values):
	    (l, h) = (0, (len(values) - 1))
	    while (l <= h):
	        m = ((l + h) // 2)
	        if (values[m] == target):
	            return m
	        elif (values[m] < target):
	            l = (m + 1)
	        elif (values[m] > target):
	            h = (m - 1)
	    return l
	values = [int(x) for x in sys.stdin.readline().split()]
	(l, r) = (values[0], values[1])
	lucky_nums = []
	generate_lucky_nums()
	lucky_nums.sort()
	result = 0
	i = l
	while (i <= r):
	    index = bin_search(i, lucky_nums)
	    next_lucky = lucky_nums[index]
	    result += (next_lucky * min(((next_lucky - i) + 1), ((r - i) + 1)))
	    i = (next_lucky + 1)
	return(result)
