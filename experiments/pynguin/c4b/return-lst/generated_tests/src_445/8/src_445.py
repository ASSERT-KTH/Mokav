def func(*args):
	ret_values = []
	
	from math import sqrt
	x = int(args[0])
	numbers = [int(i) for i in str(x)]
	count = 0
	for i in range(1, (int(sqrt(x)) + 1)):
	    if ((x % i) == 0):
	        digits = [int(j) for j in str(i)]
	        flag = 0
	        for j in digits:
	            if (j in numbers):
	                flag = 1
	                break
	        if flag:
	            count += 1
	        digits = [int(j) for j in str((x // i))]
	        flag = 0
	        for j in digits:
	            if (j in numbers):
	                flag = 1
	                break
	        if (flag and ((x // i) != i)):
	            count += 1
	ret_values.append(count)

	return ret_values
