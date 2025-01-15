def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Test the functions
c_temp = float(input("Enter temperature in Celsius: "))
print(f"{c_temp}C = {celsius_to_fahrenheit(c_temp)}F")

f_temp = float(input("Enter temperature in Fahrenheit: "))
print(f"{f_temp}F = {fahrenheit_to_celsius(f_temp)}C")
