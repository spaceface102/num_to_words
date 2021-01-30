#!/usr/bin/python3
import math
import sys

def main_output(num):
	if not num: #edge case where the number is == 0
		format_output(0, "zero")
	else:
		palabra = digits2word(num)
		format_output(num, palabra)
		return palabra

def digits2word(num):
	teens_conv =  {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen",
				   5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
	conv_10s =    {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 
				   7 : "seventy", 8: "eighty", 9: "ninety"}
	normal_base = {0: "", 1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
		   		   8: 'eight', 9: 'nine'}
	super_sufix = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", 
				   "Quintrillion", "Sextillion", "Septillion", "Octillion", "Nonillion",
				   "Decillion", "Undecillion", "Duodecillion", "Tredecillion", 
				   "Quattuordecillion", "Quindecillion", "Sexdecillion", "Septendecillion",
				   "Octodecillion", "Novemdecillion", "Vigintillion"]

	digits = list(map(lambda x: int(x), str(num))) #convert to a list of digits
	if len(digits) % 3:
		digits = [0]*(3 - len(digits)%3)+digits #ensure block of 3
	if len(digits) > len(super_sufix)*3:
		print("Bro, please use scientific notation.")
		quit()
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
				else:
					numword = conv_10s[num] + "-" + normal_base[digitslice[j+1]]
				skip_next = True
			else: #j == 2 1s place
				numword = normal_base[num]

			output_text += " " + numword
		output_text += " " + super_sufix[out_loop_num -1 - i]
	return output_text

def format_output(og_num, digit_word):
	print(og_num, "=>", digit_word)

main_output(9899999999999999)
# if len(sys.argv) > 1 and len(sys.argv) < 3:
# 	main_output(int(sys.argv[1]))
# else:
# 	main_output(int(input("Please provide a number: ")))