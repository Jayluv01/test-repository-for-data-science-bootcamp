light = input("What color is the traffic light?")
#allowed colors are red, yeelow, and green
if light == "red" or light == "yellow" or light == "green":

# One 'equal to' symbol means assignment
# If statement  is the backbone of control flows, and everyone starts with an 'If'
    if light == "green" or light == "blinking":
        print("Go")
    elif light == "yellow":
        print("Slow down")
# Else clause.
    elif light == "red":
        print("Stop")
else:
    print("Valid colors are red, yellow, and green only!")

print("")
print ("-" * 15)
print ("-" * 15)
print("")

temperature = 35
humidity = 15

if temperature > 30 or humidity < 20:
    print("Warning: Unusual weather condition detected!")
else:
    print("weather conditions are normal")
    
