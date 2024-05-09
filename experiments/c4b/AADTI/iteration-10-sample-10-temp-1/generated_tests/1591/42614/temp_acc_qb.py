def patched_func(*args):
	global_list = []
	
	
	def Solve(n):
	    if ((n % 2) == 1):
	        return (((n // 2) * n) + ((n // 2) + 1))
	    x = ((n - 2) // 2)
	    if ((x % 2) == 1):
	        return (Solve(x) * 4)
	    else:
	        return (((x // 2) * x) * 4)
	L = [0, 1, 0]
	for i in range(3, 1000):
	    L.append(Solve(i))
	x = int(args[0])
	if (x == 3):
	    global_list.append(5)
	else:
	    for i in range(1, 1000):
	        if ((x <= L[i]) and ((i % 2) == 1)):
	            global_list.append(i)
	            break
	        if ((x <= L[i]) and ((i % 2) == 0) and (((L[i] - x) % 4) == 0)):
	            global_list.append(i)
	            break
	return global_list