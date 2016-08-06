def calc_tip(bill_amount,tip_percent):
	return bill_amount*tip_percent

def tot_bill(bill_amount,tip_amount):
	return bill_amount + tip_amount

def split_bill(tot_bill,num_people):
	return tot_bill / num_people

def main():
	choice = int(raw_input("Enter 1 to calculate tip.  Enter 2 to split the bill"))
	if choice ==1:
		bill_amount = int(raw_input("What is the bill amount?"))
		tip_percent = (float(raw_input("What is the tip percent"))/100)
		tip_output = calc_tip(bill_amount,tip_percent)
		print "tip amount = " + str(tip_output)
		tot_bill_output = tot_bill(bill_amount,tip_output)
		print "total bill = " + str(tot_bill_output)
		choice2 = raw_input("Would you like to split the bill?").lower()
		if choice2 == "yes":
			num_people = int(raw_input("How many people are there?"))
			split_bill_output = round(split_bill(tot_bill_output,num_people))
			print "split bill = " + str(split_bill_output)
	elif choice ==2:
		tot_bill_output = int(raw_input("What is the bill amount?"))
		num_people = int(raw_input("How many people are there?"))
		split_bill_output = round(split_bill(tot_bill_output,num_people))
		print "split bill = " + str(split_bill_output)

if __name__ =='__main__':
	main()