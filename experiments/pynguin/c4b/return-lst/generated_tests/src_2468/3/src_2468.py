def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def mayorvalor(n):
	    aux = n[0]
	    for i in n:
	        if (aux < i):
	            aux = i
	    return aux
	
	def mes(n, m):
	    cont = 1
	    res = sum(m)
	    if (n is 0):
	        return n
	    elif (res < n):
	        return (- 1)
	    else:
	        var = mayorvalor(m)
	        suma = var
	        while (suma < n):
	            var = mayorvalor(m)
	            m.remove(var)
	            var2 = mayorvalor(m)
	            suma = (suma + var2)
	            cont += 1
	    return cont
	
	def main():
	    n = int(stdin.readline())
	    m = list(map(int, stdin.readline().split()))
	    cont = 0
	    ret_values.append(mes(n, m))
	main()

	return ret_values
