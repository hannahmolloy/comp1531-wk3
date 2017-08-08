'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(string):
	new_string = []
	seen_string = []
	s_string = string.split(" ")
	for i in range(0, len(s_string) - 1):
		
	new_string = sorted(new_string)
	return new_string
    	#print(sorted_list)
print(singlify(sentence))
