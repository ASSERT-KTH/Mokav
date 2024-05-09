def original_func(*args):
	global_list = []
	
	
	def CheckTriangle(x, y, z):
	    if ((x < (y + z)) and (y < (x + z)) and (z < (x + y))):
	        return 3
	    elif ((x == (y + z)) or (z == (x + y)) or (y == (z + x))):
	        return 2
	    else:
	        return 0
	line_of_nums = args[0]
	nums = [int(s) for s in line_of_nums.split() if s.isdigit()]
	global_list.append(nums)
	a = nums[0]
	b = nums[1]
	c = nums[2]
	d = nums[3]
	abc = CheckTriangle(a, b, c)
	abd = CheckTriangle(a, b, d)
	acd = CheckTriangle(a, c, d)
	bcd = CheckTriangle(b, c, d)
	if ((abc == 3) or (abd == 3) or (acd == 3) or (bcd == 3)):
	    global_list.append('TRIANGLE')
	elif ((abc == 2) or (abd == 2) or (acd == 2) or (bcd == 2)):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list