def func(*args):
	ret_values = []
	
	(a, b, c) = list(map(int, args[0].split()))
	nums = []
	for i in range((c + 1)):
	    if ((a * i) == c):
	        ret_values.append('Yes')
	        exit()
	    elif ((a * i) > c):
	        break
	    nums.append((a * i))
	for i in range(1, (c + 1)):
	    nums = [(x + b) for x in nums]
	    if (c in nums):
	        ret_values.append('Yes')
	        exit()
	ret_values.append('No')

	return ret_values
