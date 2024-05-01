def patched_func(*args):
	global_list = []
	
	S = args[0].split()
	n = int(S[0])
	a = int(S[1])
	b = int(S[2])
	global_list.append(min((n - a), (b + 1)))
	return global_list