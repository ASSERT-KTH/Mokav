def func(*args):
	ret_values = []
	
	horseshoes_color = args[0].split()
	count = (len(horseshoes_color) - len(list(set(horseshoes_color))))
	ret_values.append(count)

	return ret_values
