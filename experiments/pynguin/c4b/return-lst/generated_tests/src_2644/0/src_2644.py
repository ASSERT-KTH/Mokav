def func(*args):
	ret_values = []
	
	str_params = args[0]
	[n, k] = [int(s) for s in str_params.split(' ')]
	parts = (((1 + k) / 2) * k)
	if (parts <= n):
	    nod = (n / parts)
	    while (((nod % 1) != 0) | ((parts % 1) != 0)):
	        if (nod < parts):
	            if ((nod % 1) != 0):
	                nod = int(nod)
	            else:
	                nod = (nod - 1)
	            parts = (n / nod)
	        else:
	            if ((parts % 1) != 0):
	                parts = (int(parts) + 1)
	            else:
	                parts = (parts + 1)
	            nod = (n / parts)
	    numbers = [(nod * (x + 1)) for x in range(k)]
	    numbers[(k - 1)] = (n - (((((1 + k) - 1) / 2) * (k - 1)) * nod))
	    if (numbers[0] == 0):
	        ret_values.append((- 1))
	    else:
	        ret_values.append(' '.join(map(str, map(int, numbers))))
	else:
	    ret_values.append((- 1))
	"while (sum(numbers)<n):\n\n\t\n\n\n\n\t33/5 = 6.6\n\n\t33/11 = 3\n\n\t\n\n\t33/6 = 5.5\n\n\t\n\n\t24/10 = 2.4\n\n\t\n\n\t\n\n\t\n\ni = 1\n\nwhile (sum(numbers)<n) & (i<k):\n\n\twhile sum(numbers)<n:\n\n\t\tnumbers = [numbers[x]*i for x in range(k)]\n\n\t\tprint (i, numbers)\n\n\t\ti = i+1\n\nprint (numbers)\n\nif sum(numbers)>n:\n\n\tprint (-1)\n\nif sum(numbers)==n:\n\n\tprint (' '.join(map(str,numbers)))"

	return ret_values
