def original_func(*args):
	global_list = []
	
	a = int(args[0])
	lst = 'Washington,Adams,Jefferson,Madison,Monroe,Adams,Jackson,Van Buren,Harrison,Tyler,Polk,Taylor,Fillmore,Pierce,Buchanan,Lincoln,Johnson,Grant,Hayes,Garfield,Arthur,Cleveland,Harrison,Cleveland,McKinley,Roosevelt,Taft,Wilson,Harding,Coolidge,Hoover,Roosevelt,Truman,Elsenhower,Kennedy,Johnson,Nixon,Ford,Carter,Reagan'.split(',')
	global_list.append(lst[(a - 1)])
	return global_list