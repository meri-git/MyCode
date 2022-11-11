try:
	with open("E:\datafiles\sad1.txt", mode='w') as my_file:
		text = my_file.write(':(')
		print(text)
except FileNotFoundError as err:
	print('file does not exist')
	raise err
except IOError as err:
	print('IT error')
	raise err
