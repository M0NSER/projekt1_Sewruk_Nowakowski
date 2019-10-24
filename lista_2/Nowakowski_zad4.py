def temperature(cel, temperature_type):
    tempTypes=["farenheit","rankine", "kelvin"]
    result=0
    if temperature_type==tempTypes[0]:
        result=cel*9/5+32
    elif temperature_type==tempTypes[1]:
        result=(cel+ 273.15)*9/5
    elif temperature_type==tempTypes[2]:
        result = cel + 273.15
    return result

temp=temperature(33,"rankine")
print(temp)

