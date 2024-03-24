def func(*args):
	ret_values = []
	
	s = args[0]
	t = [s[i] for i in range((len(s) // 2)) if (s[i] != s[((len(s) - i) - 1)])]
	ret_values.append(['NO', 'YES'][(((len(t) <= 1) and ((len(s) % 2) == 1)) or (len(t) == 1))])

	return ret_values
