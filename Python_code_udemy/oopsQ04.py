#Temperature Converter
"""
Celsius   (0-100)c
Fahrenheit  f=(c*9/5)+32
Kelvine=c+273.15


"""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return(celsius*9/5)+32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return(fahrenheit-32)*5/9
    @staticmethod
    def celcius_to_kelvin(celsius):
        return celsius+273.15
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin-273.15
    @staticmethod
    def fahrenheit_to_kelvin(farhenheit):
        celsius=TemperatureConverter.fahrenheit_to_celsius(farhenheit)
        return TemperatureConverter.celcius_to_kelvin(celsius)
    
if __name__=="__main__":
    f=TemperatureConverter.celcius_to_kelvin(100)
    print(f)
    

