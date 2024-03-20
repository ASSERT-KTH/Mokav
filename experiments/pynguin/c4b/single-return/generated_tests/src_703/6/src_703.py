def func(*args):
	
	S = args[0].split()
	n = int(S[0])
	a = int(S[1])
	b = int(S[2])
	return(min((n - a), (b + 1)))
