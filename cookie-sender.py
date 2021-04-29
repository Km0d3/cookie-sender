# Quick and dirty script to send cookies to a URL using python used for the picoctf challenge
import os

i = 0 
while i != 30: # Number you want to go up to you can also create an array and loop it through that with a for loop
	path = "./results.txt"

	def command(i):
		os.system("curl -v --cookie \"name={0}\" http://mercury.picoctf.net:17781/check >> result.txt".format(i)) # Change cookie value and URL here
	
	i += 1
	os.system("clear")
	print("Results saved to 'result.txt'")

	
