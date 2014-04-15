password = "12345"
going = True
attemptsLeft = 5
with open("data/passwordprompt.txt") as data:
	viewable = data.read().splitlines()

while going:
	typed = input("Please Input Password: ")

	if typed == password:
		print(viewable)
		going = False
		print("Goodbye")
	else:
		def grammar():
			if attemptsLeft > 1:
				return "ies"
			else:
				return "y"
		if attemptsLeft == 0:
			going = False
			print("Ain't crackin this, bucko!")
		else:
			print("Wrong Password, Please try again. You have %s tr%s left." % (str(attemptsLeft), grammar()))
		attemptsLeft -= 1	

data.close()