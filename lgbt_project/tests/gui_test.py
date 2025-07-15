import os

def gui_test(func):
	def wrapper():
		os.system("cls")
		print(f"Func {func.__name__}")
		func()
		print(f"Testing is completed")

	return wrapper
	