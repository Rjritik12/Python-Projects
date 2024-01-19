import math

def get_user_input():
    temp_val = float(input("Enter a temperature value: "))
    temp_unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")
    return temp_val, temp_unit

def convert_temperature(temp_val, temp_unit):
    if temp_unit.lower() == "c":
        return (temp_val * (9/5)) + 32, "F"
    elif temp_unit.lower() == "f":
        return (temp_val - 32) * (5/9), "C"
    else:
        return None, None

temp_val, temp_unit = get_user_input()
converted_temp, converted_unit = convert_temperature(temp_val, temp_unit)

if converted_temp is not None:
    print("The temperature in {} is: {} degrees {}".format(converted_unit, converted_temp, converted_unit))
else:
    print("Invalid unit of measurement.")