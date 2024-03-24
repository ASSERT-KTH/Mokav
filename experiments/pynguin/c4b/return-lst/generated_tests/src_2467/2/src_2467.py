def func(*args):
	ret_values = []
	
	from sys import stdin
	
	def main():
	    num = int(stdin.readline().strip())
	    vec = [int(x) for x in stdin.readline().strip().split()]
	    long = 0
	    if (num == 0):
	        ret_values.append(num)
	    else:
	        while (long != (len(vec) - 1)):
	            mayor = vec[long]
	            suma = 0
	            c = 0
	            for j in range(long, len(vec)):
	                if (mayor <= vec[j]):
	                    mayor = vec[j]
	                    postm = j
	            vacio = vec[long]
	            vec[long] = mayor
	            vec[postm] = vacio
	            for i in range(len(vec)):
	                suma += vec[i]
	                c += 1
	                if (suma >= num):
	                    break
	            long += 1
	        if (suma < num):
	            ret_values.append((- 1))
	        else:
	            ret_values.append(c)
	main()

	return ret_values
