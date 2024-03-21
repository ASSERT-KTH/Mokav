def func(*args):
	ret_values = []
	
	S = args[0].split()
	n = int(S[0])
	a = int(S[1])
	b = int(S[2])
	ret_values.append(min((n - a), (b + 1)))

	return ret_values
