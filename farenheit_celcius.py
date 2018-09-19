temperature = float(input('Enter the temperature in degrees: '))
temperature_type = input('Enter the temperature type: ').lower()

def temp_conversion(temperature, temperature_type):
    if temperature_type == 'c' or 'celcius':
        temperature = ((temperature * (9/5)) + 32)
        temperature_type = "Farenheit"
    else:
        temperature = ((temperature - 32) / (9/5))
        temperature_type = "Celcius"
    return f'The temperature is {temperature} degrees {temperature_type}'

print(temp_conversion(temperature, temperature_type))
