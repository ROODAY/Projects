password = "12345"
going = True
choosing = False
writing = False
attemptsLeft = 5
readable = ""
x = 0
with open("data/passwordprompt.txt") as data:
	viewable = data.read().splitlines()
while x < len(viewable):
	def unshift(string):
		if string == "a":
			return "d"
		elif string == "b":
			return "e"
		elif string == "c":
			return "f"
		elif string == "d":
			return "g"
		elif string == "e":
			return "h"
		elif string == "f":
			return "i"
		elif string == "g":
			return "j"
		elif string == "h":
			return "k"
		elif string == "i":
			return "l"
		elif string == "j":
			return "m"
		elif string == "k":
			return "n"
		elif string == "l":
			return "o"
		elif string == "m":
			return "p"
		elif string == "n":
			return "q"
		elif string == "o":
			return "r"
		elif string == "p":
			return "s"
		elif string == "q":
			return "t"
		elif string == "r":
			return "u"
		elif string == "s":
			return "v"
		elif string == "t":
			return "w"
		elif string == "u":
			return "x"
		elif string == "v":
			return "y"
		elif string == "w":
			return "z"
		elif string == "x":
			return "0"
		elif string == "y":
			return "1"
		elif string == "z":
			return "2"
		elif string == "A":
			return "D"
		elif string == "B":
			return "E"
		elif string == "C":
			return "F"
		elif string == "D":
			return "G"
		elif string == "E":
			return "H"
		elif string == "F":
			return "I"
		elif string == "G":
			return "J"
		elif string == "H":
			return "K"
		elif string == "I":
			return "L"
		elif string == "J":
			return "M"
		elif string == "K":
			return "N"
		elif string == "L":
			return "O"
		elif string == "M":
			return "P"
		elif string == "N":
			return "Q"
		elif string == "O":
			return "R"
		elif string == "P":
			return "S"
		elif string == "Q":
			return "T"
		elif string == "R":
			return "U"
		elif string == "S":
			return "V"
		elif string == "T":
			return "W"
		elif string == "U":
			return "X"
		elif string == "V":
			return "Y"
		elif string == "W":
			return "Z"
		elif string == "X":
			return "0"
		elif string == "Y":
			return "1"
		elif string == "Z":
			return "2"
		elif string == "0":
			return "3"
		elif string == "1":
			return "4"
		elif string == "2":
			return "5"
		elif string == "3":
			return "6"
		elif string == "4":
			return "7"
		elif string == "5":
			return "8"
		elif string == "6":
			return "9"
		elif string == "7":
			return "A"
		elif string == "8":
			return "B"
		elif string == "9":
			return "C"
		else:
			return string

	def decode(string):
		product = ""
		letter = 0
		while letter < len(string):
			product += unshift(string[letter])

	readable += viewable[x] + "\n"
	x += 1
while going:
	typed = input("Please Input Password: ")

	if typed == password:
		choosing = True
		while choosing:
			ans = input("Would you like to read (1) or write (2)?")
			if ans == "1":
				print(readable)
				choosing = False
				going = False
				print("Goodbye")
			elif ans == "2":
				writing = True
				savethis = input("Please enter the data with format\"Login | Email | Password\"")

				def shift(string):
					if string == "a":
						return "7"
					elif string == "b":
						return "8"
					elif string == "c":
						return "9"
					elif string == "d":
						return "a"
					elif string == "e":
						return "b"
					elif string == "f":
						return "c"
					elif string == "g":
						return "d"
					elif string == "h":
						return "e"
					elif string == "i":
						return "f"
					elif string == "j":
						return "g"
					elif string == "k":
						return "h"
					elif string == "l":
						return "i"
					elif string == "m":
						return "j"
					elif string == "n":
						return "k"
					elif string == "o":
						return "l"
					elif string == "p":
						return "m"
					elif string == "q":
						return "n"
					elif string == "r":
						return "o"
					elif string == "s":
						return "p"
					elif string == "t":
						return "q"
					elif string == "u":
						return "r"
					elif string == "v":
						return "s"
					elif string == "w":
						return "t"
					elif string == "x":
						return "u"
					elif string == "y":
						return "v"
					elif string == "z":
						return "w"
					elif string == "A":
						return "7"
					elif string == "B":
						return "8"
					elif string == "C":
						return "9"
					elif string == "D":
						return "A"
					elif string == "E":
						return "B"
					elif string == "F":
						return "C"
					elif string == "G":
						return "D"
					elif string == "H":
						return "E"
					elif string == "I":
						return "F"
					elif string == "J":
						return "G"
					elif string == "K":
						return "H"
					elif string == "L":
						return "I"
					elif string == "M":
						return "J"
					elif string == "N":
						return "K"
					elif string == "O":
						return "L"
					elif string == "P":
						return "M"
					elif string == "Q":
						return "N"
					elif string == "R":
						return "O"
					elif string == "S":
						return "P"
					elif string == "T":
						return "Q"
					elif string == "U":
						return "R"
					elif string == "V":
						return "S"
					elif string == "W":
						return "T"
					elif string == "x":
						return "U"
					elif string == "Y":
						return "V"
					elif string == "Z":
						return "W"
					elif string == "0":
						return "x"
					elif string == "1":
						return "y"
					elif string == "2":
						return "z"
					elif string == "3":
						return "0"
					elif string == "4":
						return "1"
					elif string == "5":
						return "2"
					elif string == "6":
						return "3"
					elif string == "7":
						return "4"
					elif string == "8":
						return "5"
					elif string == "9":
						return "6"
					else:
						return string

				def encode(string):
					x = 0
					encoded = ""
					while x < len(string):
						encoded += shift(string[x])
						x += 1
				finished = encode(savethis) + "\n"
				data.write(finished)
				print(finished)
				shouldEnd = input("Are you done? Yes (1), No (2)")
				if shouldEnd == "1":
					writing = False
					choosing = False
					going = False
				elif shouldEnd == "2":
					writing = False
					choosing = False
				else:
					print("That is not an option")
			else:
				print("That is not an option")

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