# Q2: Write a python program using function to convert Celsius to Fahrenheit.

def temp_conversion(sel_temp):

    if(sel_temp == "f"):
        temp = float(input("Enter temperature in Celcius: "))
        return f"{temp}°C into Farenheit is: {(temp * 9/5) + 32:.2f}°F"
    elif(sel_temp == "c"):
        temp = float(input("Enter temperature in Farenheit: "))
        return f"{temp}°F into Celcius is: {(temp - 32) * 5/9:.2f}°C"
    else:
        return "Error! Please enter a valid conversion."
    
sel_temp = input("Type 'F' to convert to Farenheit or 'C' to convert to Celcius: ").lower()
temp = temp_conversion(sel_temp)
print(temp)