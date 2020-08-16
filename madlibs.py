def main():
	# write your code here
	print ("Mad libs where libs get mad.")
	print ("Start below:")
	time = input("Enter a number from 1 to 12: ")
	items = input("Enter a noun(plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ").upper()
	action = input("Enter a verb: ")
	name = name.capitalize()
	print ("/nThe story goes.../n")
	print("It was %d o\'clock whent I heard a knock at the door."%(time))
	print("I opened the door and there was a box full of %s with a note saying \"From Mr. %s.\""%(items,name))
	print("Just as I closed the door i heard a scream \"%s.\""%(scream))
	print("I froze in place and all I could do was %s."%(action))


if __name__ == '__main__':
	main()
