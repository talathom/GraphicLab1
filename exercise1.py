year = input("Enter number of years old")
month = input("Enter number of months old")

# 86400 Seconds in a Day 365 Days Per Year, 30 Per month
seconds = year * 365 * 86400
seconds += month * 30 * 86400
print("You are ", seconds ," seconds old")