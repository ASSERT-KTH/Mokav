def func(*args):
	ret_values = []
	
	n = int(args[0])
	kartu = 10
	powarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
	for i in range(len(powarray)):
	    if ((kartu + powarray[i]) == n):
	        ret_values.append('4')
	if ((kartu + 10) == n):
	    ret_values.append('15')
	elif ((n <= 10) or (n > 21)):
	    ret_values.append('0')

	return ret_values
