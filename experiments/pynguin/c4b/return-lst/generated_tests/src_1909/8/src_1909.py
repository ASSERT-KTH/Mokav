def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def sort(lis):
	    for i in range(len(lis)):
	        for j in range(len(lis)):
	            if (lis[i] < lis[j]):
	                (lis[j], lis[i]) = (lis[i], lis[j])
	    return lis
	
	def suma(lis, resul, n, i, cont):
	    if (i in range((len(lis) + 1))):
	        if (resul < n):
	            resul += lis[(- i)]
	            return suma(lis, resul, n, (i + 1), (cont + 1))
	    if (resul >= n):
	        ret_values.append(cont)
	    else:
	        ret_values.append((- 1))
	
	def main():
	    n = int(stdin.readline())
	    lis = [int(x) for x in stdin.readline().strip().split()]
	    suma(sort(lis), 0, n, 1, 0)
	main()

	return ret_values
