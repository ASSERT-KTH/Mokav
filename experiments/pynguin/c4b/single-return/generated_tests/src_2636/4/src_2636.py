def func(*args):
	
	
	def kfactorization(n, qtd):
	    if ((n == 1) or (qtd == 0)):
	        return {(- 1)}
	    if (qtd == 1):
	        return [n]
	    if (n / 2).is_integer():
	        result = [2]
	        result.extend(kfactorization(int((n / 2)), (qtd - 1)))
	        if ((- 1) in result):
	            return [(- 1)]
	        return result
	    for i in range(3, n, 2):
	        if (n / i).is_integer():
	            result = [i]
	            result.extend(kfactorization(int((n / i)), (qtd - 1)))
	            if ((- 1) in result):
	                return [(- 1)]
	            return result
	    return [(- 1)]
	if (__name__ == '__main__'):
	    (n, q) = args[0].split(' ')
	    result = kfactorization(int(n), int(q))
	    text = ''
	    for i in result:
	        text += (str(i) + ' ')
	    return(text)
