
# chocolate project cmpt 120
# This program allows a user to order chocolates. The user can choose from two types Almond and Peanut Butter. Chocolates need to ordered in whole boxes.
# Boxes consist of round and oval. Oval boxes hold 11 Almond and 4 PB candies. Round boxes hold 7 almond and 4 pb candies.
# This project was a learning excercise for cmpt 120 and intended to teach basic python usage.


#The first portion introduces the customer to the company and asks them for their name.

print ("Welcome to the Industrial Chocolate Conglomerate.")

f_name = input("Type your first name here: ")
l_name = input("Type your last name here: ")
print ("\n")
print ("Hello", f_name, l_name, "welcome to the chocolate conglomerate. The system assumes you type in your answers correctly.")


# Stage A - Asking for costs
print ("\n")
print ("Stage A - Cost Calculations\n")

print ("The default costs per item are as follows: \nA-(Almond): $2, \nB-(Peanut Butter): $1.5, \nOval Boxes: $5, \nRound Boxes: $5.5 ")

#If the user opts to they can input different prices for the chocolates and the boxes.
print (f_name, "would you like to continue using the default values?")
choice = input("Y/N: ").upper()

if choice == "Y":
	print ("\n")
	print ("Excellent we will continue to use the default costs!")
	almond    = 2.0
	pb        = 1.5
	oval      = 5.0
	round_box = 5.5
	print ("Almond:$", almond, "Peanut Butter:$", pb, "Oval Boxes:$", oval, "Round Boxes:$", round_box)

else:
	print ("\n")
	print ("Ok lets agree to a new price list. Please enter new prices as prompted.")
	almond = input("Per almond chocolate? ==>")
	pb     = input("Per peanut butter chocolate? ==>")
	oval   = input("Per oval box? ==>")
	round_box = input("Per round box? ==>")
	print ("Almond:$", almond, "Peanut Butter:$", pb, "Oval Boxes:$", oval, "Round Boxes:$", round_box)


# Stage B - Box to candy calculations

print ("\n")
print (f_name, "you can calculate your total by the number of chocolates or the number of boxes.")
by_boxes = input("Would you like to calculate your total by the number of boxes? [Y/N]: ").upper()

if by_boxes == "Y":
	print ("\nFirst select the number of oval boxes you wish to order.")
	print ("Remember that oval boxes hold 11 almond chocolates, 4 peanut butter chocoletes and cost $", oval)
	oval_total   = input("Desired number of oval boxes: ")

	print ("\nNow select the number of round boxes you wish to order.")
	print ("Remember that round boxes hold 7 almond chocolates, 4 peanut butter chocoletes and cost $", round_box)
	round_box_total = input("Desired number of round boxes: ")

	print (f_name, "you have chosen", oval_total, "oval boxes and", round_box_total, "round boxes.") 

	#these calculations refer to the oval boxes
	num_almond_oval  = float(oval_total)      * 11
	num_pb_oval      = float(oval_total)      * 4 

	print ("Tracer num_almond_oval:", num_almond_oval, "num_pb_oval:", num_pb_oval)

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

	total_cost_round_boxes = cost_almond_round     + cost_pb_round + cost_round_boxes
	order_cost             = total_cost_oval_boxes + total_cost_round_boxes

	print ("\nThe total cost of the oval boxes including chocolates was: $", total_cost_oval_boxes, "This order contains ", num_almond_oval, "almond chocolates and ", num_pb_oval, "peanut butter chocolates.")

	print ("\nThe total cost of the round boxes including chocolates was: $", total_cost_round_boxes, "This order contains ", num_almond_oval, "almond chocolates and ", num_pb_oval, "peanut butter chocolates.")
	print ("\nIn total your order will cost $", order_cost, "for the oval and round boxes.")

else:
	print ("\nExcellent let us move onto selections by the number of individual chocolates.")

# Part C From Bonbons to Boxes
######### needs clean interms of formatting and to add vales for the number of boxes and the price##############################################################

almond_selection = input("\nPlease select the number of almond chocolates you would like in your order: ")
pb_selection     = input("\nPlease select the number of peanut butter chocolates you would like to order: ")

almond_selection_boxes = float(almond_selection) // 11
pb_selection_boxes     = float(pb_selection)     // 4


if almond_selection_boxes > pb_selection_boxes:
  pb_excess           = float(pb_selection)     % 4
  almond_excess       = float(almond_selection) - 11 * float(pb_selection_boxes)
  oval_boxes_required = pb_selection_boxes
  print("Tracer pb_excess: ", pb_excess, "almond_excess: ", almond_excess)
  print("Oval boxes ordered: ", oval_boxes_required, "Excess almonds: ", almond_excess, "Excess peanut butter: ", pb_excess)


elif almond_selection_boxes < pb_selection_boxes:
  almond_excess       = float(almond_selection) % 11
  pb_excess           = float(pb_selection)     - 4 * float(almond_selection_boxes)
  oval_boxes_required = almond_selection_boxes
  print("Tracer pb_excess: ", pb_excess, "almond_excess: ", almond_excess)
  print("Oval boxes ordered: ", oval_boxes_required, "Excess almonds: ", almond_excess, "Excess peanut butter: ", pb_excess)

else:
  almond_excess       = float(almond_selection) % 11
  pb_excess           = float(pb_selection)     % 4
  oval_boxes_required = almond_selection_boxes
  print("Tracer almond excess: ", almond_excess, "Pb excess: ", pb_excess)
  print("Oval boxes ordered: ", oval_boxes_required, "Excess almonds: ", almond_excess, "Excess peanut butter: ", pb_excess)


# C+ Bonus section
# If the user would like to calculate the bonus section we first figure out the number of round boxes needed based on the previous user inputs.
# after that we figure out the excess chocolate from the order and attach a cost to it. This is compared against the oval box values and the most economic choice is highlighted.

print("\n")
print (f_name, "would you like to do the bonus calculations?")
bonus = input("Y/N: ").upper()

if bonus == "Y":
	almond_selection_round_boxes = float(almond_selection) // 7
	pb_selection_round_boxes     = float(pb_selection)     // 4

	if almond_selection_round_boxes > pb_selection_round_boxes:
		pb_excess_round      = float(pb_selection)     % 4 
		almond_excess_round  = float(almond_selection) - 7 * float(pb_selection_round_boxes)
		round_boxes_required = pb_selection_round_boxes
		print ("Number of round boxes: ", round_boxes_required, " Almond excess: ", almond_excess_round, " PB excess: ", pb_excess_round)
	elif pb_selection_round_boxes > almond_selection_round_boxes:
		almond_excess_round  = float(almond_selection) % 7
		pb_excess_round      = float(pb_selection)     - 4 * float(almond_selection_round_boxes) 
		round_boxes_required = almond_selection_round_boxes
		print ("Number of round boxes: ", round_boxes_required, " Almond excess: ", almond_excess_round, " PB excess: ", pb_excess_round)
	else:
		almond_excess_round  = float(almond_selection) % 7
		pb_excess_round      = float(pb_selection)     % 4 
		round_boxes_required = almond_selection_round_boxes
		print ("Number of round boxes: ", round_boxes_required, " Almond excess: ", almond_excess_round, " PB excess: ", pb_excess_round)		

	print("\n")
	oval_loss  = almond_excess * float(almond) + pb_excess * float(pb)
	round_loss = almond_excess_round * float(almond) + pb_excess_round * float(pb)
	print("Tracer Cost of excess chocolates in oval box orders  =====> $", oval_loss )
	print("Tracer Cost of excess chocolates in round box orders =====> $", round_loss)
	if oval_loss > round_loss:
		print("\n")
		print ("You should buy", round_boxes_required, "Round Boxes because the loss if producing Oval Boxes (", oval_loss, ") is greater than the loss if producing Round Boxes (", round_loss, ")")
	elif oval_loss < round_loss:
		print("\n")
		print("You should buy", oval_boxes_required, "Oval Boxes because the loss if producing Round Boxes (", round_loss, ") is greater than the loss if producing Oval Boxes (", oval_loss, ")")

else:
	print("Great moving onto secret code production.")
	
#Part D - Secret code 
# import random allows the use of random.randint which generates a random number in a range.
import random

code = (f_name[0].lower() + l_name[-1].upper() + "**" + "A" + str(almond) + "**" + "B" + str(pb) + "**" + str(oval_boxes_required) + "**" + str(random.randint(0,oval_boxes_required)) + "**")
# I was unsure of how I should add traces to this portion as I tested as each addition to the code variable as it was being constructed.

#If the value of the length of code is positive it wont return a remainder where as if it does return a remainder we know its odd.
if len(code) % 2 == 0:
  print("\n")
  print("Based on your order this is your secret code:")
  print(code + "Even")
else:
  print("\n")
  print(code + "Odd")



