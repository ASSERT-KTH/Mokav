def func(*args):
	ret_values = []
	
	num = args[0]
	g = 0
	nums = ['4', '44', '444', '7', '77', '777', '47', '74', '474', '447', '744', '774', '747', '477']
	if (num in nums):
	    ret_values.append('YES')
	elif (num not in nums):
	    for i in nums:
	        if ((int(num) % int(i)) == 0):
	            ret_values.append('YES')
	            g += 1
	            break
	    if (g == 0):
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
