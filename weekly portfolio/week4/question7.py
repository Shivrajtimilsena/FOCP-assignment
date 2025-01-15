def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temps = []
for _ in range(6):
    temp = input("Enter temperature (e.g., 25C): ").strip()
    if temp[-1].upper() == 'C':
        temps.append(float(temp[:-1]))
    else:
        print("Invalid input format.")

if temps:
    print(f"Maximum: {max(temps)}C, Minimum: {min(temps)}C, Mean: {sum(temps)/len(temps):.2f}C")
