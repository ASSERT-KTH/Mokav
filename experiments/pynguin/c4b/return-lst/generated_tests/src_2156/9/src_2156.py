def func(*args):
	ret_values = []
	
	import sys
	from decimal import Decimal
	
	def main():
	    nstr = input.readline()
	    n = Decimal(nstr)
	    if ((n >= (- 128)) and (n <= 127)):
	        output.write('byte')
	    elif ((n >= (- 32768)) and (n <= 32767)):
	        output.write('short')
	    elif ((n >= (- 2147483648)) and (n <= 2147483647)):
	        output.write('int')
	    elif ((n >= Decimal('-9223372036854775808')) and (n <= Decimal('9223372036854775807'))):
	        output.write('long')
	    else:
	        output.write('BigInteger')
	
	def run():
	    global input, output
	    input = sys.stdin
	    output = sys.stdout
	    main()
	if (__name__ == '__main__'):
	    run()

	return ret_values
