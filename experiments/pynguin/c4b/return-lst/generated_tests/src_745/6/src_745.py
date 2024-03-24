def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	sum = 0
	sum += (a * int((b / 5)))
	sum += (int((a / 5)) * (b % 5))
	if (((a % 5) + (b % 5)) >= 5):
	    sum += ((((a % 5) + (b % 5)) % 5) + 1)
	ret_values.append(sum)

	return ret_values
