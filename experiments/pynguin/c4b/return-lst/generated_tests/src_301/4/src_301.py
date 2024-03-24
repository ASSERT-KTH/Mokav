def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    n = int(args[0])
	    line = str(args[1]).split()
	    line = [int(it) for it in line]
	    n %= sum(line)
	    if (n == 0):
	        n = sum(line)
	    temp = 0
	    for i in range(7):
	        temp += line[i]
	        if (temp >= n):
	            ret_values.append((i + 1))
	            break

	return ret_values
