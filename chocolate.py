# chocolate project cmpt 120
############# consider changing values from float or at least have key values round down to 2 decimal spots ###############################




#The first portion introduces the customer to the company and asks them for their name.

print ("Welcome to the Industrial Chocolate Conglomerate.")
print ("Please provide your Oompa Loompa with your first and last name.")

f_name = input("Type your first name here: ")
l_name = input("Type your last name here: ")
print ("\n")
print ("Hello", f_name, l_name, "welcome to the chocolate conglomerate.")
print ("Keep in mind that the Oompa Loompa who will be completing your order assumes you will be typing correctly.")

print ("\n")
# Stage A - Asking for costs
print ("Stage A - Cost Calculations\n")

print ("The default costs per item are as follows: \nA-(almond): $2, \nB-(Peanut Butter): $1.5, \nOval Boxes: $5, \nRound Boxes: $5.5 ")


print (f_name, "would you like to continue using the default values or would you like to select your own prices?")
# .upper makes the answer the user inputs upper case. This made testing easier more than anything else...
choice = input("Y/N: ").upper()

# if the user types Y then we continue to use the default costs
if choice == "Y":
	print ("Excellent we will continue to use the default costs!")
	almond = 2.0
	pb     = 1.5
	oval   = 5.0
	round_box = 5.5
	print (almond, pb, oval, round_box)
# if the user types anything other than Y we go ask the user for input and assign new values to the price list.
else:
	print ("Ok lets agree to a new price list.")
	almond = input("How much would you like to pay per almond chocolate? ==>")
	pb     = input("How much would you like to pay per peanut butter chocolate? ==>")
	oval   = input("How much would you like to pay per oval box? ==>")
	round_box = input("How much would you like to pay per round box? ==>")
	print (almond, pb, oval, round_box)

# Stage B - Box to candy calculations

print (f_name, "you can calculate your total by the number of chocolates or the number of boxes.")
by_boxes = input("Would you like to calculate your total by the number of boxes? [Y/N]: ").upper()

if by_boxes == "Y":
	print ("\nFirst select the number of oval boxes you wish to order.")
	print ("Remember that oval boxes hold 11 Almond chocolates, 4 Peanut Butter Chocoletes and cost $", oval)
	oval_total   = input("Desired number of oval boxes: ")

	print ("\nNow select the number of round boxes you wish to order.")
	print ("Remember that round boxes hold 7 Almond chocolates, 4 Peanut Butter Chocoletes and cost $", round_box)
	round_box_total = input("Desired number of round boxes: ")

	print (f_name, "you have chosen", oval_total, "oval boxes and", round_box_total, "round boxes.") 

	#these calculations refer to the oval boxes
	num_almond_oval  = float(oval_total)      * 11
	num_pb_oval      = float(oval_total)      * 4 

	# print ("Tracer num_almond_oval:", num_almond_oval, "num_pb_oval:", num_pb_oval)

	cost_almond_oval = num_almond_oval        * float(almond)
	cost_pb_oval     = num_pb_oval            * float(pb)
	cost_oval_boxes  = float(oval_total)      * float(oval)

	total_cost_oval_boxes  = cost_almond_oval + cost_pb_oval + cost_oval_boxes

	# these calculations refer to the round boxes
	num_almond_round  = float(round_box_total)  * 7
	num_pb_round      = float(round_box_total)  * 4

	cost_almond_round = num_almond_round        * float(almond)
	cost_pb_round     = num_pb_round            * float(pb)
	cost_round_boxes  = float(round_box_total)  * float(round_box)

	total_cost_round_boxes = cost_almond_round + cost_pb_round + cost_round_boxes

	print ("\nThe total cost of the oval boxes including chocolates was: $", total_cost_oval_boxes)
	print ("To be more specific we need", num_almond_oval, "almond chocolates and", num_pb_oval, "peanut butter chocolates.")
	print ("\nThe total cost of the round boxes including chocolates was: $", total_cost_round_boxes)
	print ("Specifically we need", num_almond_round, "almond chocolates and", num_pb_round, "peanut butter chocolates.")

else:
	print ("Excellent let us move onto selections by the number of individual chocolates.")

# Part C From Bonbons to Boxes


almond_selection = input("\nPlease select the number of almond chocolates you would like in your order: ")
pb_selection     = input("\nPlease select the number of peanut butter chocolates you would like to order: ")

almond_selection_boxes = float(almond_selection) // 11
pb_selection_boxes     = float(pb_selection)     // 4

#Here I used an if statement to calculate the excess chocolates. If the order has a lot more Almond candies then peanutbutter candies we wont have any remainder
# for the pb candies because the extra will just go into more boxes to get to the total specified by the almond quantity.

if almond_selection_boxes > pb_selection_boxes:
	print ("You will need to order", almond_selection_boxes, "oval boxes.")
	excess_almond = float(almond_selection) % 11
	print ("Tracer: excess_almond: ", excess_almond)

# If the almond order and the pb order are similar (A=116 pb=42) then each candy requires the same number of boxes. Here the remainder of each candy is important because it wont be added to the next box.

elif almond_selection_boxes == pb_selection_boxes:
	print ("You will need to order", almond_selection_boxes, "oval boxes.")
	excess_almond = float(almond_selection) % 11
	excess_pb     = float(pb_selection)     % 4 
	print ("Tracer: excess_almond: ", excess_almond, "excess_pb", excess_pb)	

# Here the Pb candies are the bulk of the order (A=5 pb=27534) in cases such as this the remainder of the almond candies doesnt matter because they will be added to another box to satisfy the need for more pb candies.
else:
	print ("You will need to order", pb_selection_boxes, "oval boxes.")
	excess_pb     = float(pb_selection)     % 4
	print ("Tracer: excess_pb: ", excess_pb)

