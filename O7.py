def price(a):
	global count
	if a <= 0: return (count)
	count += 0.25
	a -= 140
	return price(a)
print(f'${4+price(int(input()))}')