password = "12345"
going = True
choosing = False
writing = False
attemptsLeft = 5
readable = ""
x = 0
with open("data/passwordprompt.txt", "r+") as data:
	viewable = data.read().splitlines()
	while x < len(viewable):
		def unoffset(offset, letter):
			return chr(ord(letter) + offset)

		def decode(string):
			x = 0
			decoded = ""
			while x < len(string):
				decoded += unoffset(-3, string[x])
				x += 1
			return decoded

		readable += decode(viewable[x]) + "\n"
		x += 1
	while going:
		typed = input("Please Input Password: ")

		if typed == password:
			choosing = True
			while choosing:
				ans = input("Would you like to read (1) or write (2)? ")
				if ans == "1":
					print(readable)
					choosing = False
					going = False
					print("Goodbye!")
				elif ans == "2":
					writing = True
					savethis = input("Please enter the data with format \"Login | Email | Password\" ")
					finished = ""
					def offset(offset, letter):
						return chr(ord(letter) + offset)

					def encode(string):
						x = 0
						encoded = ""
						while x < len(string):
							encoded += offset(3, string[x])
							x += 1
						return encoded

					finished = encode(savethis) + "\n"
					data.write(finished)
					print(finished," was saved to data")
					shouldEnd = input("Are you done? Yes (1), No (2) ")
					if shouldEnd == "1":
						writing = False
						choosing = False
						going = False
						print("Goodbye!")
					elif shouldEnd == "2":
						writing = False
					else:
						print("That is not an option!")
				else:
					print("That is not an option!")

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