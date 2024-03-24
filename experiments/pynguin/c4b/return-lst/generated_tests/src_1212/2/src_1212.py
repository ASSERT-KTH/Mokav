def func(*args):
	ret_values = []
	
	s = args[0]
	cnt = sum(((s[i] != s[((- i) - 1)]) for i in range((len(s) // 2))))
	ret_values.append(('YES' if ((cnt == 1) or ((cnt == 0) and ((len(s) % 2) == 1))) else 'NO'))

	return ret_values
