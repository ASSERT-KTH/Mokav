def func(*args):
	ret_values = []
	
	string = args[0]
	ans = string.count('VK')
	string = string.replace('VK', ' ')
	ans += (1 if (('VV' in string) or ('KK' in string)) else 0)
	ret_values.append(ans)

	return ret_values
