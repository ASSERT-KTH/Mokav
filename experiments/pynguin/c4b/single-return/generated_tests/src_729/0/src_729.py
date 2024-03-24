def func(*args):
	
	(a, b) = [int(x) for x in args[0].split()]
	d = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
	dzerosinrange = {10: 9, 100: 180, 1000: 2700, 10000: 36000, 100000: 450000}
	answer = 0
	i = a
	while (i <= b):
	    if ((i in dzerosinrange) and (((i * 10) - 1) <= b)):
	        answer += (6 * dzerosinrange[i])
	        for digit in range(1, 10):
	            answer += (d[digit] * (i + dzerosinrange[i]))
	        i = (i * 10)
	    else:
	        test = i
	        while (test > 0):
	            digit = (test % 10)
	            answer += d[digit]
	            test = (test // 10)
	        i = (i + 1)
	return(answer)
