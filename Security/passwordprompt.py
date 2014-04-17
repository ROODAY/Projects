#Import Random Number function
from random import randrange

#Open nececessary files
with open("data/passwordpromptdata.txt", "r+") as data:
	with open("data/passwordpromptoffsets.txt", "r+") as offsets:
		with open("data/passwordpromptpassword.txt", "r+") as rawpassword:
			with open("data/passwordpromptconfig.txt", "r+") as config:

				#Read config and prepare necessary variables

				#Define Booleans
				running = True
				choosing = False
				writing = False

				#Load, prepare, and unscramble password from textfile
				def showpassword(password, offset):
					counter = 0
					passwordfinal = ""
					while counter < len(password):
						passwordfinal += chr(ord(password[counter]) - offset)
						counter += 1
					return passwordfinal
				password = rawpassword.read().splitlines()
				password = showpassword(password[1], int(password[0]))

				#Run main loop
				attemptsLeft = 5
				while running:

					#Prompt password input
					typed = input("Please Input Password: ")

					#Checks input against known password
					if typed == password:

						#Ask what the user wants to do
						choosing = True
						ans = input("Would you like to view entries (1), add an entry (2), delete an entry (3), edit an entry (4), or change password (5)? ")
						while choosing:

							#Option 1 unscrambles then prints entries 
							if ans == "1":
								#Prepare and decrypt data
								viewabledata = data.read().splitlines()
								viewableoffsets = offsets.read().splitlines()

								readable = ""
								decodecount = 0
								while decodecount < len(viewabledata):
									def unoffset(letter, offset):
										if (ord(letter) - letter) < 32:
											return chr(((ord(letter) - offset) - 32) + 127)
										else:
											return chr(ord(letter) - offset)
									def decode(string, offsetnum):
										stringpos = 0
										decoded = ""
										while stringpos < len(string):
											decoded += unoffset(string[stringpos], int(offsetnum))
											stringpos += 1
										return decoded

									readableprereq = decode(viewabledata[decodecount], viewableoffsets[decodecount])
									readable += readableprereq[2:] + "\n"
									decodecount += 1

								#Print data and end script
								print(readable)
								choosing = False
								running = False
								print("Goodbye!")

							#Option 2 adds an entry
							elif ans == "2":

								#Prompts user for entry to add
								writing = True
								savethis = input("Please enter the data with format \"Login | Email | Password\" ")

								#Encyrpts entry by converting to ASCII code and shifting by offset. It will wrap code if the offset pushes it too far
								finisheddata = ""
								finishedoffset = 0
								randoffset = randrange(10,100)
								def offset(offset, letter):
									if (ord(letter) + offset) > 126:
										return chr(((ord(letter) + offset) - 126) + 31)
									else:
										return chr(ord(letter) + offset)
								def encode(string, offsetnum):
									stringpos = 0
									encoded = ""
									while stringpos < len(string):
										encoded += offset(offsetnum, string[stringpos])
										stringpos += 1
									return encoded
								finisheddata = encode(savethis,randoffset) + "\n"
								finishedoffset = str(randoffset) + "\n"

								#Saves entry to data, saves offset to offsets prints what was saved
								data.write(finisheddata)
								offsets.write(finishedoffset)
								print(finisheddata," was saved to data")

								#Prompts user if they are done adding entries
								shouldEnd = input("Are you done adding? Yes (1), No (2) ")

								#Option 1 ends the script
								if shouldEnd == "1":
									writing = False
									choosing = False
									running = False
									print("Goodbye!")

								#Option 2 prompts user for new antry to add
								elif shouldEnd == "2":
									writing = False

								#Any answer that isn't an option ends the script
								else:
									print("That is not an option!")
									writing = False
									choosing = False
									running = False
									print("Goodbye!")

							#Any answer that isn't an option ends the script
							else:
								print("That is not an option!")
								writing = False
								choosing = False
								running = False
								print("Goodbye!")

					#If entered password does not match, it shows the user amount of tries remaining, and continues until tries run out
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

#Close all opened files in order of nest
			config.close()
		rawpassword.close()
	offsets.close()
data.close()