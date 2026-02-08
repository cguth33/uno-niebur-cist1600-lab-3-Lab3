# Name: Carter Guthrie
# Date: 2/8/2025
# Assignment: Lab 3
# Purpose: Approximate Pi using a series and measure time

import math
import time

def main():
    realPi = math.pi
    
    # Ask user for decimal precision (limit iterations for speed)
    precision = int(input("How many iterations for the series? (e.g., 1000000): "))
    
    start = time.time()
    
    # Calculate pi using the Gregory-Leibniz series
    my_pi = 0
    denominator = 1
    for i in range(precision):
        if i % 2 == 0:
            my_pi += 4 / denominator
        else:
            my_pi -= 4 / denominator
        denominator += 2
        
    end = time.time()
    
    elapsedTime = end - start
    print(f"Approximated Pi: {my_pi}")
    print(f"Difference from math.pi: {abs(realPi - my_pi)}")
    print(f"Time taken: {elapsedTime} seconds")

if __name__ == '__main__':
    main()
