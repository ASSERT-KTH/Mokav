def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	b = True
	while b:
	    if (((a[0] + a[1]) > a[2]) and ((a[0] + a[2]) > a[1]) and ((a[1] + a[2]) > a[0])):
	        ret_values.append('TRIANGLE')
	        b = False
	    elif (((a[0] + a[1]) > a[3]) and ((a[0] + a[3]) > a[1]) and ((a[1] + a[3]) > a[0])):
	        ret_values.append('TRIANGLE')
	        b = False
	    elif (((a[0] + a[2]) > a[3]) and ((a[0] + a[3]) > a[2]) and ((a[2] + a[3]) > a[0])):
	        ret_values.append('TRIANGLE')
	        b = False
	    elif (((a[2] + a[1]) > a[3]) and ((a[2] + a[3]) > a[1]) and ((a[1] + a[3]) > a[2])):
	        ret_values.append('TRIANGLE')
	        b = False
	    else:
	        a = sorted(a)
	        c = a[(len(a) - 1)]
	        d = a[(len(a) - 2)]
	        if ((a[1] + d) >= c):
	            ret_values.append('SEGMENT')
	        elif ((a[0] + a[1]) >= d):
	            ret_values.append('SEGMENT')
	        else:
	            ret_values.append('IMPOSSIBLE')
	        b = False

	return ret_values
