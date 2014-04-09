n = int(raw_input("Enter a number: "))
series = [1]

while len(series) < n:
	if len(series) == 1:
		series.append(1)
	else:
		series.append(series[-1] + series[-2])

print "The Fibonacci sequence to the number you entered is " + series