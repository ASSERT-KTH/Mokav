def func(*args):
	ret_values = []
	
	time = 240
	[n, k] = [int(x) for x in args[0].split()]
	time -= k
	problems = 0
	i = 1
	while ((time - (5 * i)) >= 0):
	    problems += 1
	    time -= (5 * i)
	    i += 1
	    if (problems == n):
	        break
	ret_values.append(problems)

	return ret_values
