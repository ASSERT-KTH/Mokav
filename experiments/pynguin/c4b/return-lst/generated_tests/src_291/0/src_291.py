def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = 0
	max = 0
	while True:
	    max = (max + ((2 ** k) * 5))
	    min = (max - ((2 ** k) * 5))
	    if (min <= n <= max):
	        break
	    k += 1
	if (((n - min) % (2 ** k)) == 0):
	    who = ((n - min) // (2 ** k))
	elif (((n - min) % (2 ** k)) != 0):
	    who = (((n - min) // (2 ** k)) + 1)
	if (who == 1):
	    ret_values.append('Sheldon')
	elif (who == 2):
	    ret_values.append('Leonard')
	elif (who == 3):
	    ret_values.append('Penny')
	elif (who == 4):
	    ret_values.append('Rajesh')
	elif (who == 5):
	    ret_values.append('Howard')

	return ret_values
