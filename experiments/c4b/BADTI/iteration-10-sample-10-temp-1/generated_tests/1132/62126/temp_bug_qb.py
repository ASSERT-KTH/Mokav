def original_func(*args):
	global_list = []
	
	num = args[0]
	nums = ['4', '44', '444', '7', '77', '777', '47', '74', '474', '447', '744', '774', '747', '477']
	if (num in nums):
	    global_list.append('YES')
	elif (num not in nums):
	    for i in nums:
	        if ((int(num) % int(i)) == 0):
	            global_list.append('YES')
	            break
	        else:
	            global_list.append('NO')
	            break
	else:
	    global_list.append('NO')
	return global_list