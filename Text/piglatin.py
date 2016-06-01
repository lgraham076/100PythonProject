Enter file contents here# Pig Latin - Pig Latin is a game of alterations played on the English language 
# game. To create the Pig Latin form of an English word the initial consonant 
# sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" 
# would yield anana-bay). Read Wikipedia for more information on rules.

from sys import argv

def piglatin(word):
	word=word.lower()
	print(word[1:]+word[0]+"ay")

if len(argv) <= 1:
	print("Received no arguments using example word: Strawberry")
	piglatin("Strawberry")
else:
	piglatin(argv[1])
