#!/usr/bin/python3

import sys

#Exchange the first and last chosen letters until middle reached
def reverse_word(word,beg,end):
	tmp_word=list(word)
	#Word is reversed when indexes cross each other in middle
	if beg > end:
		return tmp_word

	#Switch letters
	tmp_end = word[end]
	tmp_word[end] = tmp_word[beg]
	tmp_word[beg] = tmp_end

	#Progress indexes
	beg += 1
	end -= 1

	return reverse_word(tmp_word,beg,end)


#MAIN
if len(sys.argv) >= 2:
	#Grab each argument from the command line to be reversed
	for i in range(1, len(sys.argv)):
		word=str(sys.argv[i])
		wordlength = len(word)
		#If there is only one letter don't need to reverse
		if wordlength > 1:
			beg = 0 #Beginning letter of word
			end = wordlength-1 #Ending letter of word
			word="".join(reverse_word(word,beg,end)[:])

		print(word)
else:
	print ("Must include a string argument to reverse")
