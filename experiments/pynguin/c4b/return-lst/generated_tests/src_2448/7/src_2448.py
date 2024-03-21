def func(*args):
	ret_values = []
	
	n = int(args[0])
	listnames = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	i = 0
	t = False
	c = 5
	listcount = [1, 1, 1, 1, 1]
	if (1 <= n <= 5):
	    ret_values.append(listnames[(n - 1)])
	elif (n == 6):
	    ret_values.append('Sheldon')
	else:
	    while (t == False):
	        while (i < 5):
	            listcount[i] = (listcount[i] * 2)
	            c = (c + listcount[i])
	            i = (i + 1)
	            if (c >= n):
	                ret_values.append(listnames[(i - 1)])
	                t = True
	                break
	        i = 0

	return ret_values
