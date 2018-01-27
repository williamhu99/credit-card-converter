# This program decodes the information stored in a credit card based on IATA Encoding
proper_input = False
input1 = ""
input2 = ""

# Asks the user for input
while proper_input == False:
	proper_input = True
	input1 = raw_input("Please enter a string of binary digits to decode: ")
	if len(input1) < 7:
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

# Implements the lookup table for IATA Encoding
def lookup(next_string):
	lookup_string = next_string[0:6]
	if lookup_string == "000000":
		return " SP "
	elif lookup_string == "000010":
		return "0"
	elif lookup_string == "000011":
		return "P"
	elif lookup_string == "000100":
		return "("
	elif lookup_string == "000101":
		return "H"
	elif lookup_string == "000110":
		return "8"
	elif lookup_string == "000111":
		return "X"
	elif lookup_string == "001000":
		return "$"
	elif lookup_string == "001001":
		return "D"
	elif lookup_string == "001010":
		return "4"
	elif lookup_string == "001011":
		return "T"
	elif lookup_string == "001101":
		return "L"
	elif lookup_string == "010001":
		return "B"
	elif lookup_string == "010010":
		return "2"
	elif lookup_string == "010011":
		return "R"
	elif lookup_string == "010101":
		return "J"
	elif lookup_string == "010111":
		return "Z"
	elif lookup_string == "011001":
		return "F"
	elif lookup_string == "011010":
		return "6"
	elif lookup_string == "011011":
		return "V"
	elif lookup_string == "011100":
		return "."
	elif lookup_string == "011101":
		return "N"
	elif lookup_string == "100001":
		return "A"
	elif lookup_string == "100010":
		return "1"
	elif lookup_string == "100011":
		return "Q"
	elif lookup_string == "100100":
		return ")"
	elif lookup_string == "100101":
		return "I"
	elif lookup_string == "100110":
		return "9"
	elif lookup_string == "100111":
		return "Y"
	elif lookup_string == "101001":
		return "E"
	elif lookup_string == "101010":
		return "5"
	elif lookup_string == "101011":
		return "U"
	elif lookup_string == "101100":
		return "--"
	elif lookup_string == "101101":
		return "M"
	elif lookup_string == "110001":
		return "C"
	elif lookup_string == "110010":
		return "3"
	elif lookup_string == "110011":
		return "S"
	elif lookup_string == "110101":
		return "K"
	elif lookup_string == "111001":
		return "G"
	elif lookup_string == "111010":
		return "7"
	elif lookup_string == "111011":
		return "W"
	elif lookup_string == "111100":
		return "/"
	elif lookup_string == "111101":
		return "O"
	else:
		return "NULL"

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
	while input1[0:7] != "0001011":
		input1 = input1[1:len(input1)]
		if len(input1) < 7:
			print "Error. No start sentinel."
			break

	# Starts decoding
	input1 = input1[7:len(input1)]

	while len(input1) >= 7:
		next_string = input1[0:7]
		input1 = input1[7:len(input1)]

		# First checks for the Field Sentinel
		if next_string == "1111100":
			print " FS ",
		elif next_string == "0111110":
			print " ES ",
			if len(input1) >= 7:
				print lookup(input1[0:6:-1]),
			break
		else:
			print lookup(next_string[0:6:-1]),

# Decodes the input string with the most significant bit on the right
def decodeR(input1):
	# Finds the start sentinel (SS)
	while input1[0:7] != "1010001":
		input1 = input1[1:len(input1)]
		if len(input1) < 7:
			print "Error. No start sentinel."
			break

	# Starts decoding
	input1 = input1[7:len(input1)]

	while len(input1) >= 7:
		next_string = input1[0:7]
		input1 = input1[7:len(input1)]

		# First checks for the Field Sentinel
		if next_string == "0111110":
			print " FS ",
		elif next_string == "1111100":
			print " ES ",
			if len(input1) >= 7:
				print lookup(input1[0:7]),
			break
		else:
			print lookup(next_string[0:7]),

if input3 == '16':
	input1 = convert(input1)
	print "Your input in binary is: " + input1

if input2 == 'L':
	decodeL(input1)
else:
	decodeR(input1)