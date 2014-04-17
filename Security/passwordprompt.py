#Import Random Number function
from random import randrange

#Open nececessary files
with open("data/passwordpromptdata.txt", "r+") as data:
	with open("data/passwordpromptoffsets.txt", "r+") as offsets:
		with open("data/passwordpromptpassword.txt", "r+") as rawpassword:
			with open("data/passwordpromptconfig", "r+") as config:

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
								viewable = data.read().splitlines()
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

								#Encyrpts entry
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

								#Saves entry to data, prints what was saved
								data.write(finished)
								print(finished," was saved to data")

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