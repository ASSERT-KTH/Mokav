def func(*args):
	ret_values = []
	
	nums = list(map(int, args[0].split()))
	e = nums[0]
	i = nums[1]
	dmg = nums[2]
	passed = False
	if ((dmg is e) or (dmg is i) or (dmg is 0)):
	    ret_values.append('Yes')
	else:
	    index = 0
	    while (((e * index) < dmg) and ((i * index) < dmg)):
	        if (((dmg - (e * index)) % i) is 0):
	            passed = True
	            break
	        elif (((dmg - (i * index)) % e) is 0):
	            passed = True
	            break
	        index += 1
	    if passed:
	        ret_values.append('Yes')
	    else:
	        ret_values.append('No')

	return ret_values
