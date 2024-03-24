def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def partition(lista):
	    (pivote, menores, mayores) = (lista[0], [], [])
	    for x in range(1, len(lista)):
	        if (lista[x] < pivote):
	            menores.append(lista[x])
	        else:
	            mayores.append(lista[x])
	    return (menores, [pivote], mayores)
	
	def quicksort(lista):
	    if (len(lista) < 2):
	        return lista
	    (menores, medio, mayores) = partition(lista)
	    return ((quicksort(menores) + medio) + quicksort(mayores))
	
	def main():
	    n = int(stdin.readline())
	    m = [int(arr_temp) for arr_temp in stdin.readline().strip().split()]
	    m = quicksort(m)
	    i = (len(m) - 1)
	    s = 0
	    k = 0
	    while (i >= 0):
	        if (s < n):
	            s = (s + m[i])
	            k += 1
	        i -= 1
	    if (s < n):
	        ret_values.append('-1')
	    else:
	        ret_values.append(k)
	main()

	return ret_values
