def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Get input and convert
temp = input("Enter temperature in C: ").strip()
if temp[-1].upper() == 'C':
    c_temp = float(temp[:-1])
    print(f"{c_temp}C = {celsius_to_fahrenheit(c_temp)}F")
else:
    print("Invalid input format.")
