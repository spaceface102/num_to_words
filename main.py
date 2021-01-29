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
	super_sufix = ["", "", "thousand", "million", "billion", "trillion", "quadrillion", 
				   "quintrillion", "sextillion", "septillion", "octillion", "nonillion",
				   "decillion"]

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
				prefix = normal_base[num] + "-hundred"

			elif j == 1: #currently in the 10s place
				if num == 1: #all the teens are here
					prefix = teens_conv[digitslice[j+1]]
					skip_next = True
				else:
					prefix = conv_10s[num]

			else: #j == 2 1s place
				prefix = normal_base[num]

			output_text += " " + prefix
		modifier = super_sufix[out_loop_num - i]
		output_text += " " + modifier
	return output_text

def format_output(og_num, digit_word):
	print(og_num, "=>", digit_word)

if len(sys.argv) > 1 and len(sys.argv) < 3:
	main_output(int(sys.argv[1]))
else:
	main_output(int(input("Please provide a number: ")))


#Ivan
# num2wrd = {1: 'One', 2: 'Two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
# 		   8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
# 		   15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
# num2wrd2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
# 			8: 'eighty', 9: 'ninety'}
# def number(num):
# 	if 0 <= num <= 19:
# 		return num2wrd[num]
# 	elif 20 <= num <= 99:
# 		tens, remainder = divmod(num, 10) # == int(num,10), num%10
# 		return num2wrd2[tens - 2] + ' - ' + num2wrd[remainder] if remainder else num2wrd2[tens - 2]
# number(52)