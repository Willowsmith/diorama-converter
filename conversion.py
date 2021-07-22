val = input("Enter your starting size: ")
scale = input("Enter scale you wish to convert to ")


try:
    is_value = int(val)
except ValueError:
    print("Please only use positive numbers greater than 0.")

try:
    is_scale = int(scale)
except ValueError:
    print("Please only use positive numbers greater than 0.")

if val or scale < 1:
    print("Please only use positive numbers greater than 0.")
else:
    final = val / scale
    print("Your dirorama value is " + str(final))


