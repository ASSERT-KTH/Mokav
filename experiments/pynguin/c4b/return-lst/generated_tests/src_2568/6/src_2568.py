def func(*args):
	ret_values = []
	
	n = args[0]
	numbers = []
	i = 0
	k = 0
	numbers.append('')
	while (i < len(n)):
	    if (n[i] != ' '):
	        numbers[k] += n[i]
	    else:
	        k += 1
	        numbers.append('')
	    i += 1
	for i in range(len(numbers)):
	    numbers[i] = int(numbers[i])
	numbers.sort()
	a = numbers[0]
	b = numbers[1]
	c = numbers[2]
	d = numbers[3]
	if (((a + b) > c) or ((a + c) > d) or ((b + c) > d)):
	    ret_values.append('TRIANGLE')
	elif (((a + b) == c) or ((a + c) == d) or ((b + c) == d) or ((a + b) == d)):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
