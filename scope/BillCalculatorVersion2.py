tip_amount = 0
total_bill = 0
split_amount = 0

def calculate_bill(original_bill_amount,tip_percentage=18,split_number=1):
	global tip_amount
	tip_amount = original_bill_amount * tip_percentage / 100
	global total_bill
	total_bill = original_bill_amount+tip_amount
	global split_amount
	split_amount = total_bill/split_number

def main():
	original_bill_amount = 100
	calculate_bill(original_bill_amount,split_number=3)	
	print "original bill is " + str(original_bill_amount)
	print "tip amount is " + str(tip_amount)	
	print "total bill is " + str(total_bill)
	print "split amount is " + str(split_amount)

if __name__ == '__main__':
	main()