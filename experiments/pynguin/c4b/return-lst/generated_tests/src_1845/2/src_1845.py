def func(*args):
	ret_values = []
	
	a = [int(i) for i in args[0].split()]
	m = int(a[0])
	d = int(a[1])
	if ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
	    if (d <= 5):
	        ret_values.append('5')
	    else:
	        ret_values.append('6')
	if (m == 2):
	    if (d == 1):
	        ret_values.append('4')
	    else:
	        ret_values.append('5')
	if ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
	    if (d <= 6):
	        ret_values.append('5')
	    else:
	        ret_values.append('6')

	return ret_values
