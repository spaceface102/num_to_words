#!/usr/bin/python3
import math
import sys

def main_output(num):
	if not num: #edge case where the number is == 0
		print(num, "=>", "zero")
	else:
		digits = num2digits(num)
		print(digits2word(digits))

def num2digits(num):
	power = int(math.log10(num)) #how many digits in num (minus 1 since start count at 0)
	each_digit = list()
	for cur_power in range(power, -1, -1): #count down from power inclusive to -1 exclusive by -1
		each_digit.append(int(num/(10**cur_power)))
		num -= each_digit[-1]*(10**cur_power) #remove the newest digit from num.
	return each_digit

def digits2word(digits):
	weird_conv = {2: 'twen', 3: 'thir', 5: 'fif', 8: 'eigh'} #not eightty its eighty
	normal_base = {1 : "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 
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
		for j, num in enumerate(digitslice):
			if num == 0:
				continue 

			if j == 0:
				prefix = normal_base[num]
				sufix = "-hundred"

			elif j == 1: #currently in the 10s place
				#prefix
				if (digitslice[j]*10 + digitslice[j+1]) == 10:
					prefix = "ten"
				elif num in weird_conv: #part of group of prefixes that change: 2, 3, 5
					prefix = weird_conv[num]
				else: #normal 10s place
					prefix = normal_base[num]
				
				#sufix teen of ty
				if digitslice[j+1]: #if digitslice == 0 then current num is 10
					if num == 1:
						sufix = "teen"
					else:
						sufix = "ty"
				else: #sufix for 10
					sufix = ""
				
			else: #j == 2 1s place
				prefix = normal_base[num]
				sufix = "" #no sufix for the 1s place!

			output_text += " " + prefix + sufix
		modifier = super_sufix[out_loop_num - i]
		output_text += " " + modifier
	return output_text

main_output(110_710)

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
