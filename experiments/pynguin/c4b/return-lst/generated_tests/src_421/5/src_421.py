def func(*args):
	ret_values = []
	
	x = (int(args[0]) + 1)
	while True:
	    a = [str(y) for y in str(x)]
	    if (len(set(a)) == len(str(x))):
	        ret_values.append(x)
	        break
	    else:
	        x += 1
	        continue

	return ret_values
