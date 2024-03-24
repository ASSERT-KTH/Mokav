def func(*args):
	ret_values = []
	
	a = int(args[0])
	lst = 'Washington,Adams,Jefferson,Madison,Monroe,Adams,Jackson,Van Buren,Harrison,Tyler,Polk,Taylor,Fillmore,Pierce,Buchanan,Lincoln,Johnson,Grant,Hayes,Garfield,Arthur,Cleveland,Harrison,Cleveland,McKinley,Roosevelt,Taft,Wilson,Harding,Coolidge,Hoover,Roosevelt,Truman,Eisenhower,Kennedy,Johnson,Nixon,Ford,Carter,Reagan'.split(',')
	ret_values.append(lst[(a - 1)])

	return ret_values
