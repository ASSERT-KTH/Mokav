def func(*args):
	
	(a, b, c) = list(map(int, args[0].split()))
	mas = []
	mas.append(((a + b) + c))
	mas.append((((a + a) + b) + b))
	mas.append((((a + c) + c) + a))
	mas.append((((b + c) + c) + b))
	return(min(mas))
