name = str( input("Please Enter Your name: "))
print (f"Hello And Welcome {name} in our tip calculator:)")
Total_bill= float( input(f"Please Enter The Total Amount Of the bill {name} : ") )
tip_perc = int( input("What percentage tip would you like to give? "))
Total_People= int( input("How many people to split the bill? ") )
tip_inperc = tip_perc/100
total_tip = Total_bill * tip_inperc
Total_amount = Total_bill + total_tip
bill_person = Total_amount / Total_People
final = round(bill_person, 2)
print(f"Each person should pay: ${final}")

close = input("press enter to exit")
