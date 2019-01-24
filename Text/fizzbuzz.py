#!/usr/bin/python3

# -*- coding: utf-8 -*-

#Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead
#of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five
#print “FizzBuzz”.


def fizzbuzz(beg,end):
	for i in range(beg,(end+1)):
		str=""
		if i % 3 is 0:
			str+="fizz"
		if i % 5 is 0:
			str+="buzz"

		if str is "":
			print(i)
		else:
			print(str)



if __name__=="__main__":
	fizzbuzz(0,100)
