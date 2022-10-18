sam = float(0)
def f():
	global sam
	try: num = int(input())
	except: return sam
	sam += num
	return f()
print(f())