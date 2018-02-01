# This program decodes the information stored in a credit card based on ABA Encoding
proper_input = False
input1 = ""
input2 = ""

# Asks the user for input
while proper_input == False:
	proper_input = True
	input1 = raw_input("Please enter a string of binary or hexadecimal digits to decode: ")
	if len(input1) < 5:
		proper_input = False
		print "The string is too short."
	else:
		for char in input1:
			if char < '0' or (char > '9' and char < 'A') or char > 'F':
				proper_input = False
				print "Invalid string."
				break

proper_input = False

# Asks whether the most significant bit is on the left or the right
while proper_input == False:
	input2 = raw_input("Enter 'L' if the most significant bit is on the left or 'R' if the most significant bit is on the right: ")
	if input2 == 'L' or input2 == 'R':
		proper_input = True
	else:
		print "Invalid input."

proper_input = False

# Asks whether the input is hexadecimal or binary
while proper_input == False:
	input3 = raw_input("Enter '2' if the input is in binary or '16' if the input is in hex: ")
	if input3 == '2' or input3 == '16':
		proper_input = True
	else:
		print "Invalid input."

# Implements the lookup table for ABA Encoding
# ND = not a digit
def lookup(next_string):
	lookup_string = next_string[0:4]
	if lookup_string == "0000":
		return "0"
	elif lookup_string == "0001":
		return "1"
	elif lookup_string == "0010":
		return "2"
	elif lookup_string == "0011":
		return "3"
	elif lookup_string == "0100":
		return "4"
	elif lookup_string == "0101":
		return "5"
	elif lookup_string == "0110":
		return "6"
	elif lookup_string == "0111":
		return "7"
	elif lookup_string == "1000":
		return "8"
	elif lookup_string == "1001":
		return "9"
	else:
		return "ND"

# Converts a hexadecimal string into a binary string
def convert(input1):
	if len(input1) == 0:
		return ""
	else:
		digit = input1[0:1]
		if digit == "0":
			return "0000" + convert(input1[1:len(input1)])
		elif digit == "1":
			return "0001" + convert(input1[1:len(input1)])
		elif digit == "2":
			return "0010" + convert(input1[1:len(input1)])
		elif digit == "3":
			return "0011" + convert(input1[1:len(input1)])
		elif digit == "4":
			return "0100" + convert(input1[1:len(input1)])
		elif digit == "5":
			return "0101" + convert(input1[1:len(input1)])
		elif digit == "6":
			return "0110" + convert(input1[1:len(input1)])
		elif digit == "7":
			return "0111" + convert(input1[1:len(input1)])
		elif digit == "8":
			return "1000" + convert(input1[1:len(input1)])
		elif digit == "9":
			return "1001" + convert(input1[1:len(input1)])
		elif digit == "A":
			return "1010" + convert(input1[1:len(input1)])
		elif digit == "B":
			return "1011" + convert(input1[1:len(input1)])
		elif digit == "C":
			return "1100" + convert(input1[1:len(input1)])
		elif digit == "D":
			return "1101" + convert(input1[1:len(input1)])
		elif digit == "E":
			return "1110" + convert(input1[1:len(input1)])
		elif digit == "F":
			return "1111" + convert(input1[1:len(input1)])
		else:
			return "NULL"

# Decodes the input string with the most significant bit on the left
def decodeL(input1):
	# Finds the start sentinel (SS)
	while input1[0:5] != "10110":
		input1 = input1[1:len(input1)]
		if len(input1) < 5:
			print "Error. No start sentinel."
			break

	# Starts decoding
	input1 = input1[5:len(input1)]

	while len(input1) >= 5:
		next_string = input1[0:5]
		input1 = input1[5:len(input1)]

		# First checks for the Field Sentinel
		if next_string == "10110":
			print " FS ",
		elif next_string == "11111":
			print " ES ",
			if len(input1) >= 5:
				print lookup(input1[0:4]),
			break
		else:
			print lookup(next_string[0:4]),

# Decodes the input string with the most significant bit on the right
def decodeR(input1):
	# Finds the start sentinel (SS)
	while input1[0:5] != "11010":
		input1 = input1[1:len(input1)]
		if len(input1) < 5:
			print "Error. No start sentinel."
			break

	# Starts decoding
	input1 = input1[5:len(input1)]

	while len(input1) >= 5:
		next_string = input1[0:5]
		input1 = input1[5:len(input1)]

		# First checks for the Field Sentinel
		if next_string == "10110":
			print " FS ",
		elif next_string == "11111":
			print " ES ",
			if len(input1) >= 5:
				temp = input1[0:4]
				print lookup(temp[::-1]),
			break
		else:
			temp = next_string[0:4]
			print lookup(temp[::-1]),

if input3 == '16':
	input1 = convert(input1)
	print "Your input in binary is: " + input1

if input2 == 'L':
	decodeL(input1)
else:
	decodeR(input1)