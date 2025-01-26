unit_of_hours = 24*60
name_of_unit = "hours"


def total_days(no_of_days):
    if no_of_days > 0:
       return f"{no_of_days} days are {unit_of_hours} {name_of_unit}"
    else:
        return "please enter a positive value!"


user_input = input("Enter your number here \n")
if user_input.isdigit():
   user_input_number = int(user_input)
   calculated_value = total_days(user_input_number)
   print(calculated_value)
else:
    print("Please enter Numeric value")





