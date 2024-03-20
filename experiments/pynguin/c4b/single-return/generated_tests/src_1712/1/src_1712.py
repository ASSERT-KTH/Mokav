def func(*args):
	
	(lambda x, nx: return((int(nx) if (sum(map(int, nx)) > sum(map(int, x))) else x)))(*(lambda x, p: (x, ((x[:p] + str((int(x[p]) - 1))) + (((len(x) - p) - 1) * '9'))))(*(lambda x: (x, (min(([(x[1:].find(str(i)) + 1) for i in range(9) if (x[1:].find(str(i)) != (- 1))] + [len(x)])) - 1)))(args[0])))
