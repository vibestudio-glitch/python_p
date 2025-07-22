#gb_tb_real_size
print("Choose the unit (GB or TB):")
user_unit = input(">")

# Set conversion rate based on chosen unit
if user_unit.lower() == "tb":
    rate = 1000000000000 / 1099511627776
elif user_unit.lower() == "gb":
    rate = 1000000000 / 1073741824
else:
    print("Unknown unit entered.")
    exit()

print("Enter the advertised storage amount:")
input_value = input(">")
input_value = float(input_value)

# Calculate and round the actual storage size
real_value = round(input_value * rate, 2)

print("Real usable space is", real_value, user_unit.upper())
