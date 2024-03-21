def func(*args):
	ret_values = []
	
	from itertools import chain
	from itertools import combinations
	from functools import reduce
	data = args[0]
	ss = int(data.split(' ')[0])
	nn = int(data.split(' ')[1])
	base = (((nn ** 2) + nn) / 2)
	result = []
	lss = 0
	i = int((ss / base))
	if (i == 0):
	    ret_values.append((- 1))
	elif ((i != 0) and ((ss % base) == 0)):
	    for x in range(1, nn):
	        result.append(str((i * x)))
	        lss += (i * x)
	    result.append(str((ss - lss)))
	    ret_values.append(' '.join(result))
	else:
	
	    def primefactors(n):
	        f = 2
	        while ((f * f) <= n):
	            while ((n % f) == 0):
	                (yield f)
	                n //= f
	            f += 1
	        if (n > 1):
	            (yield n)
	    prime = list(primefactors(ss))
	
	    def powerset(iterable):
	        primeall = sorted(list(set(list(chain.from_iterable((combinations(prime, r) for r in range((len(prime) + 1))))))))
	        del primeall[0]
	        primenew = []
	        for i in primeall:
	            i = list(i)
	            primenew.append(reduce((lambda x, y: (x * y)), i))
	        primenew = list(set(primenew))
	        primenew.sort(reverse=True)
	        lss = 0
	        for x in primenew:
	            if (((ss % x) == 0) and ((x * base) <= ss)):
	                result = [str((x * y)) for y in range(1, nn)]
	                for i in result:
	                    lss += int(i)
	                break
	        if (lss == 0):
	            result = [str(y) for y in range(1, nn)]
	            for z in result:
	                lss += int(z)
	        result.append(str(int((ss - lss))))
	        ret_values.append(' '.join(result))
	    powerset(prime)

	return ret_values
