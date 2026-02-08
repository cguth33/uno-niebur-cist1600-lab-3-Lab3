# Name: Carter Guthrie
# Date: 2/8/2025
# Assignment: Lab 3
# Purpose: Convert Fahrenheit to Celsius

def main():
    # Prompt the user for a Fahrenheit temperature
    tempF = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert that temperature to celsius
    # Formula: (F - 32) * 5/9
    tempC = (tempF - 32) * 5 / 9
    
    # Output converted temperature rounded to 1 decimal place
    print(f"{tempF} is {round(tempC, 1)} degrees Celsius.")

if __name__ == '__main__':
    main()