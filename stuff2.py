# Let there be two variables, Westbound and Eastbound. 
# One variable (one or the other) can only be active at all times. 
# If Westbound is active (or true), eastbound cannot be active (or false)
# Because the flow of traffic only goes one way for 5 minutes at a time, we switch when we reach that point
# something similar would be if westbound traffic = 5 then
# westbound traffic would be false and eastbound traffic would be true, same applies for vice versa

east_bound_traffic = 0
west_bound_traffic = 1
if east_bound_traffic == True and west_bound_traffic == True:
    print("False")

if east_bound_traffic == True and west_bound_traffic == False:
    print("True")

if east_bound_traffic == False and west_bound_traffic == True:
    print("True")

if east_bound_traffic == False and west_bound_traffic == False:
    print("True")
