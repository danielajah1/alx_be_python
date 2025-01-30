FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    # Use the FAHRENHEIT_TO_CELSIUS_FACTOR to calculate Celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
   
    # Use the CELSIUS_TO_FAHRENHEIT_FACTOR to calculate Fahrenheit
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")

    while True:
        try:
            # User input for temperature
            temp = float(input("Enter the temperature to convert: "))
            
            # User input for the unit
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                # Convert Celsius to Fahrenheit
                result = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {result:.2f}°F")
            elif unit == 'F':
                # Convert Fahrenheit to Celsius
                result = convert_to_celsius(temp)
                print(f"{temp}°F is {result:.2f}°C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

        # Check if the user wants to perform another conversion
        another = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
