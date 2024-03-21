def func(*args):
	ret_values = []
	
	(call, performance, day) = (int(x) for x in args[0].split())
	i = 1
	calls_per_day = set()
	performances_per_day = set()
	while ((i * call) <= day):
	    calls_per_day.add((i * call))
	    i += 1
	i = 1
	while ((i * performance) <= day):
	    performances_per_day.add((i * performance))
	    i += 1
	ans = (calls_per_day & performances_per_day)
	ret_values.append(len(ans))

	return ret_values
