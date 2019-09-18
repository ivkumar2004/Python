
def mathstable():
	"""Function to generate table from sequence 1 to 12, Number get from user"""
	tableInt = int(input("Enter the number to generate its multiples: "))
	for sequence in range(1,13):
		print ("%s x %s = %s"%(tableInt,sequence,tableInt*sequence))
	return

if __name__ == "__main__":
	exitOperation = False
	while exitOperation != True:
		ynString = str(input("Do you want to continue generating table (y/n): ")).strip().lower()
		if ynString == "y":
			mathstable()
		elif ynString == "n":
			exitOperation = True
		else:
			print ("Illegal string %s"%ynString)
