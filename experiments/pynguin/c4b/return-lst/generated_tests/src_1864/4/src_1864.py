def func(*args):
	ret_values = []
	
	(n, k) = list(map(int, args[0].strip().split(' ')))
	L = (n // k)
	import bisect
	
	def div(n):
	    if (n == 1):
	        return [1]
	    elif (n == 2):
	        return [1, 2]
	    else:
	        K = int((n ** 0.5))
	        temp1 = []
	        temp2 = []
	        for i in range(1, (K + 1)):
	            if ((n % i) == 0):
	                temp1 += [i]
	                temp2 += [(n // i)]
	        if (temp1[(- 1)] == temp2[(- 1)]):
	            temp2 = temp2[1:]
	        ans = (temp1 + temp2[::(- 1)])
	        return ans
	if (((k * (k + 1)) // 2) > n):
	    ret_values.append((- 1))
	else:
	    TTT = div(n)
	    temp = ((k * (k + 1)) // 2)
	    L = (n // temp)
	    K = (bisect.bisect_right(TTT, L) - 1)
	    L = TTT[K]
	    T = ((n - (temp * L)) // L)
	    ans = []
	    for i in range(1, (k + 1)):
	        if (i != k):
	            ans += [(i * L)]
	        else:
	            ans += [((i + T) * L)]
	    if (k == 1):
	        ret_values.append(n)
	    else:
	        ret_values.append(*ans)

	return ret_values
