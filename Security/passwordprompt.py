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
			return chr(ord(letter) - offset)

		def decode(string, offsetnum):
			stringpos = 0
			decoded = ""
			while stringpos < len(string):
				decoded += unoffset(string[stringpos], int(offsetnum))
				stringpos += 1
			return decoded

		offsetprereq = viewable[decodecount]
		readableprereq = decode(viewable[decodecount], offsetprereq[0])
		readable += readableprereq[1:] + "\n"
		decodecount += 1

	while running:
		typed = input("Please Input Password: ")

		if typed == password:
			choosing = True
			ans = input("Would you like to read (1) or write (2)? ")
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
					randoffset = randrange(3,6)
					def offset(offset, letter):
						return chr(ord(letter) + offset)

					def encode(string, offsetnum):
						stringpos = 0
						encoded = ""
						while stringpos < len(string):
							encoded += offset(offsetnum, string[stringpos])
							stringpos += 1
						return encoded

					finished = str(randoffset) + encode(savethis,randoffset) + "\n"
					data.write(finished)
					print(finished," was saved to data")
					shouldEnd = input("Are you done adding? Yes (1), No (2) ")
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