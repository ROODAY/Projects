# do this for random offset: for(var i = 0; i <= 96; i++){ encrypt(letter, i); }, add it like i + string
from random import randrange

with open("data/passwordprompt.txt", "r+") as data:
	viewable = data.read().splitlines()

	password = "12345"
	running = True
	choosing = False
	writing = False
	attemptsLeft = 5
	readable = ""
	decodecount = 0

	while decodecount < len(viewable):
		def unoffset(letter, offset):
			if (ord(letter) - offset) < 32:
				return chr(127 - (offset - (ord(letter) - 32)))
			elif (ord(letter) - offset) > 32:
				return chr(ord(letter) + offset)

		def decode(string, offsetnum):
			stringpos = 0
			decoded = ""
			while stringpos < len(string):
				decoded += unoffset(string[stringpos], int(offsetnum))
				stringpos += 1
			return decoded

		offsetprereq = str(viewable[decodecount])
		finaloffset = str(offsetprereq[0]) + str(offsetprereq[1])
		readableprereq = decode(viewable[decodecount], int(finaloffset))
		readable += readableprereq[2:] + "\n"
		decodecount += 1

	while running:
		typed = str(input("Please Input Password: "))

		if typed == password:
			choosing = True
			ans = str(input("Would you like to read (1) or write (2)? "))
			while choosing:
				if ans == "1":
					print(readable)
					choosing = False
					running = False
					print("Goodbye!")
				elif ans == "2":
					writing = True
					savethis = input("Please enter the data with format \"Login : Email : Password\" ")
					finished = ""
					def offset(offset, letter):
						if (ord(letter) + offset) > 126:
							return chr(((ord(letter) + offset) - 126) + 31)
						elif (ord(letter) + offset) < 126:
							return chr(ord(letter) + offset)

					def encode(string):
						stringpos = 0
						randoffset = randrange(10,100)
						encoded = str(randoffset)
						while stringpos < len(string):
							encoded += offset(randoffset, string[stringpos])
							stringpos += 1
						return encoded

					finished = encode(savethis) + "\n"
					data.write(finished)
					print(finished," was saved to data")
					shouldEnd = str(input("Are you done adding? Yes (1), No (2) "))
					if shouldEnd == "1":
						writing = False
						choosing = False
						running = False
						print("Goodbye!")
					elif shouldEnd == "2":
						writing = False
						ans = "2"
					else:
						print("That is not an option!")
						writing = False
						choosing = False
						running = False
						print("Goodbye!")
				else:
					print("That is not an option!")
					writing = False
					choosing = False
					running = False
					print("Goodbye!")

		else:
			def grammar():
				if attemptsLeft > 1:
					return "ies"
				else:
					return "y"
			if attemptsLeft == 0:
				running = False
				print("Ain't crackin this, bucko!")
			else:
				print("Wrong Password, Please try again. You have %s tr%s left." % (str(attemptsLeft), grammar()))
			attemptsLeft -= 1	

data.close()