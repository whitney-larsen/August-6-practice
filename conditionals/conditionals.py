if "Whitney" > "Philip":
	print "My name is greater"
elif "Philip" > "Whitney":
	print "Your name is greater"
else:
	print "Our names are equal!"

date = int(raw_input("What is today's date?"))

if date >= 15:
	print "We are halfway there"
else:
	print "The month is still young"

today = (raw_input("What day of the week is it?")).lower()

if today == "monday":
	print "yay class day"
elif today == "tuesday":
	print "sight it's only Tuesday"
elif today == "wednesday":
	print "Humpday!"
elif today == "thursday":
	print "#tbt"
elif today == "friday":
	print "TGIF!"
else:
	print "Yeah, it's the weekend"

age = int(raw_input("What is your age?"))

if age >= 18:
	print "Yay I can vote!"
else:
	print "Aww, I cannot vote"

if age >= 21:
	print "I can vote and go to the bar"
elif age >= 18:
	print "I can vote but I can't go to the bar"
else:
	print "I cannot vote or go to the bar"

if 8%2 == 1:
	print "The number 8 is odd"
elif 8%2 == 0:
	print "The number 8 is even"


if 8%2 ==0 and 9%2 ==0:
	print "Both numbesr are even"
if 8%2==0 and 9%2==1:
	print "8 is even and 9 is odd"
else:
	print "Both numbers are odd"

favorite_color = raw_input("What is your favorite color?").lower()

if favorite_color =="blue":
	print "My favorite color is blue"
else:
	print "My favorite color is not blue"

if favorite_color == "blue" or favorite_color == "red" or favorite_color == "yellow":
	print "My favorite color is a primary color"
else:
	print "My favorite color is a secondary color"



