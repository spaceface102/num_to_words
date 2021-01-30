#!/usr/bin/python3
import math
import sys

def main_output(num):
	if not num: #edge case where the number is == 0
		format_output(0, "zero")
	else:
		digits = num2digits(num)
		format_output(num, digits2word(digits))

def num2digits(num):
	power = int(math.log10(num)) #how many digits in num (minus 1 since start count at 0)
	each_digit = list()
	for cur_power in range(power, -1, -1): #count down from power inclusive to -1 exclusive by -1
		each_digit.append(int(num/(10**cur_power)))
		num -= each_digit[-1]*(10**cur_power) #remove the newest digit from num.
	return each_digit

def digits2word(digits):
	teens_conv = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen",
				  5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 
				  9: "nineteen"}
	conv_10s = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 
				7 : "seventy", 8: "eighty", 9: "ninety"}
	normal_base = {1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
		   		   8: 'eight', 9: 'nine'}
	super_sufix = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", 
				   "Quintrillion", "Sextillion", "Septillion", "Octillion", "Nonillion",
				   "Decillion", "Undecillion", "Duodecillion", "Tredecillion", 
				   "Quattuordecillion", "Quindecillion", "Sexdecillion", "Septendecillion",
				   "Octodecillion", "Novemdecillion", "Vigintillion"]

	if len(digits) % 3:
		digits = [0]*(3 - len(digits)%3)+digits #ensure block of 3
	out_loop_num = int(len(digits)/3)
	output_text = ""
	for i in range(out_loop_num):
		digitslice = digits[3*i:3*i+3]
		skip_next = False
		for j, num in enumerate(digitslice):
			if skip_next or num == 0: #there is no word related with zero 
				continue 
		
			if j == 0:
				numword = normal_base[num] + "-hundred"

			elif j == 1: #currently in the 10s place
				if num == 1: #all the teens are here
					numword = teens_conv[digitslice[j+1]]
					skip_next = True
				else:
					numword = conv_10s[num]

			else: #j == 2 1s place
				numword = normal_base[num]

			output_text += " " + numword
		'''every group of three digits is a new super sufix, say if the number
		is 123 vs the number 1234 is now officially in the thousands. 1234560 would
		be in the millions. The first group of three numbers does not have a super
		sufix, but every group after it does. Since we start processing the most
		significant bit first, and we start counting from 0 with i, the index 
		related with out_loop_num (which tells us how many groups of three there are)
		- 1 - i tells us which super_sufix we are currently using. So in the same
		way we are processing first the group of three digits that are most significant
		and finish with the group of three that are the least signifcant, we are doing
		the same with super_sufix!''' 
		output_text += " " + super_sufix[out_loop_num -1 - i]
	return output_text

def format_output(og_num, digit_word):
	print(og_num, "=>", digit_word)

if len(sys.argv) > 1 and len(sys.argv) < 3:
	main_output(int(sys.argv[1]))
else:
	main_output(int(input("Please provide a number: ")))