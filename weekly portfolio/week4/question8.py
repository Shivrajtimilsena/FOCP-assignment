def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temps = []
while True:
    temp = input("Enter temperature in 'C' or press Enter to finish: ").strip()
    if not temp:  # Terminate on empty input
        break
    if temp[-1].upper() == 'C':
        temps.append(float(temp[:-1]))
    else:
        print("Invalid input format.")

if temps:
    print(f"Maximum: {max(temps)}C, Minimum: {min(temps)}C, Mean: {sum(temps)/len(temps):.2f}C")
else:
    print("No temperatures entered.")
