def func(*args):
	ret_values = []
	
	inD = str(args[0]).split()
	inD = [int(val) for val in inD]
	k = inD[0]
	a = inD[1]
	b = inD[2]
	N = 0
	a = ((a - k) if ((a % k) == 0) else (a - (a % k)))
	b = (b - (b % k))
	N = ((b - a) // k)
	ret_values.append(N)

	return ret_values
