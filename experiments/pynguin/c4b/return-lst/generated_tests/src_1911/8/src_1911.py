def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def main():
	    n = int(stdin.readline())
	    month = [int(y) for y in stdin.readline().split()]
	    cont = 0
	    suma = 0
	    controler = 0
	    while (suma < n):
	        pos = 0
	        mas = 0
	        for i in range(len(month)):
	            controler += month[i]
	            if (month[i] == n):
	                suma = month[i]
	                cont += 1
	                break
	        if (suma != n):
	            for i in range(len(month)):
	                if (mas < month[i]):
	                    mas = month[i]
	                    pos = i
	            if (controler < n):
	                cont = (- 1)
	                break
	            month[pos] = 0
	            suma += mas
	            cont += 1
	        else:
	            break
	    ret_values.append(cont)
	main()

	return ret_values
