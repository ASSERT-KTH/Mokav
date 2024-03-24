def func(*args):
	
	return(next((a for a in range((int(args[0]) + 1), 12345) if (len(set(str(a))) == len(str(a))))))
