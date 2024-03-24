def func(*args):
	ret_values = []
	
	(a, x, y) = map(int, args[0].split())
	if ((y > 0) and ((y % a) != 0) and (x > (- a)) and (x < a)):
	    if (((y // a) == 0) or ((y // a) == 1) or ((y // a) == 2)):
	        if ((y // a) == 0):
	            if ((x > ((- a) / 2)) and (x < (a / 2))):
	                ret_values.append(1)
	                exit()
	            else:
	                ret_values.append((- 1))
	                exit()
	        elif ((y // a) == 1):
	            if ((x > ((- a) / 2)) and (x < (a / 2))):
	                ret_values.append(2)
	                exit()
	            else:
	                ret_values.append((- 1))
	                exit()
	        else:
	            if (x == 0):
	                ret_values.append((- 1))
	                exit()
	            if (x > 0):
	                ret_values.append(4)
	                exit()
	            else:
	                ret_values.append(3)
	                exit()
	    else:
	        z = ((y - (3 * a)) // (2 * a))
	        ans = (4 + (3 * z))
	        k = ((y - (3 * a)) - ((2 * a) * z))
	        if (k < a):
	            if ((x > ((- a) / 2)) and (x < (a / 2))):
	                ans += 1
	            else:
	                ret_values.append((- 1))
	                exit()
	        elif (k > a):
	            ans += 2
	            if (x > 0):
	                ans += 1
	            if (x == 0):
	                ret_values.append((- 1))
	                exit()
	        ret_values.append(ans)
	        exit()
	ret_values.append((- 1))

	return ret_values
