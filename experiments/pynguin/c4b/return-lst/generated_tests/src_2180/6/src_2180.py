def func(*args):
	ret_values = []
	
	i = args[0]
	let = max(i)
	ret_values.append((let * i.count(let)))

	return ret_values
