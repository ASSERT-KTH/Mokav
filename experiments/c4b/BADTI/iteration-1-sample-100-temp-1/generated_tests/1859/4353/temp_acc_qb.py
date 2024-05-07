def patched_func(*args):
	global_list = []
	
	s = args[0]
	t = (3 + (s[0] > 'f'))
	p = s.find('ru', (t + 1))
	global_list.append((((((s[:t] + '://') + s[t:p]) + '.ru') + ' /'[((p + 2) < len(s))]) + s[(p + 2):]))
	return global_list