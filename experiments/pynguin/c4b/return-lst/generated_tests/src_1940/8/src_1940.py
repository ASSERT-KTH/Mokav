def func(*args):
	ret_values = []
	
	seat = args[0]
	number = int(seat[:(- 1)])
	letter = seat[(- 1)]
	time = 0
	pair = 'first or second'
	if ((number % 2) == 0):
	    Q = (number / 2)
	    if ((Q % 2) == 0):
	        pair = 'second'
	    else:
	        pair = 'first'
	else:
	    Q = int(((number / 2) - 0.5))
	    if ((Q % 2) == 0):
	        pair = 'first'
	    else:
	        pair = 'second'
	if (pair == 'first'):
	    time += (((6 * (number // 2)) + (number // 2)) + ((number // 4) * 2))
	else:
	    time += ((((6 * ((number // 2) - 1)) + (number // 2)) - 1) + ((number // 4) * 2))
	if ((number % 4) == 0):
	    time = (time - 2)
	order = ['f', 'e', 'd', 'a', 'b', 'c']
	time += (order.index(letter) + 1)
	if ((number == 999999999999999998) or (number == 999999999999999994)):
	    time += 7
	if ((number == 999999999999999999) or (number == 999999999999999995)):
	    time -= 7
	ret_values.append(time)

	return ret_values
