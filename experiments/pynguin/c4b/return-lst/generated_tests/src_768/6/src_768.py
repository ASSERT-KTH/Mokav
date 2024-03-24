def func(*args):
	ret_values = []
	
	s = args[0]
	t = (3 + (s[0] > 'f'))
	p = s.find('ru', (t + 1))
	ret_values.append((((((s[:t] + '://') + s[t:p]) + '.ru') + ' /'[((p + 2) < len(s))]) + s[(p + 2):]))

	return ret_values
