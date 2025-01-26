import datetime
# get the current date and time
now = datetime.datetime.now()
# show the message
print("Current Date and Time is:")
# show time in specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# new program

color_list = ["red", "green", "black", "white"]
print(color_list[0], color_list[-1])