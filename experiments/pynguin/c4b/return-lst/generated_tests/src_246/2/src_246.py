def func(*args):
	ret_values = []
	
	
	def lucky(n):
	    mes = 'YES'
	    while ((n >= 1) and (mes == 'YES')):
	        ld = (n % 10)
	        if ((ld == 7) or (ld == 4)):
	            mes = 'YES'
	            n = (n // 10)
	        else:
	            mes = 'NO'
	            n = (- 1)
	    return mes
	
	def main(n):
	    if (lucky(n) == 'YES'):
	        MESS = 'YES'
	    else:
	        for i in range(1, (n + 1)):
	            MESS = 'NO'
	            if ((lucky(i) == 'YES') and (MESS == 'NO')):
	                if ((n % i) == 0):
	                    MESS = 'YES'
	                    break
	                else:
	                    MESS = 'NO'
	    return MESS
	N = int(args[0])
	ret_values.append(main(N))

	return ret_values
