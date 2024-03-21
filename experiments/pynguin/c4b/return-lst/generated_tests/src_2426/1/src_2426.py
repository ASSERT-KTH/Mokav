def func(*args):
	ret_values = []
	
	numbers = list(map(int, args[0].split()))
	if ((numbers[0] > 0) and (numbers[0] <= 100)):
	    if ((numbers[1] < numbers[0]) and (numbers[2] < numbers[0])):
	        if ((numbers[0] - numbers[1]) <= numbers[2]):
	            ret_values.append((numbers[0] - numbers[1]))
	        else:
	            ret_values.append((numbers[2] + 1))

	return ret_values
