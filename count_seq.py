# Author: Kristin Towns
# GitHub: kristinlashun
# Date: 2/28/2024
"""
Description: This file contains a generator function named count_seq that generates a sequence of strings
where each term is derived by counting and describing the count of the numbers in the previous term.
The sequence starts with "2" and each subsequent term describes the count of digits in the previous term.
This implementation does not require arguments and generates the sequence indefinitely.
"""

def count_seq():
    term = "2"  # Initial term of the sequence
    while True:
        yield term  # Yield the current term
        next_term = ""  # Initialize the next term as an empty string
        count = 1  # Initialize count of the current digit
        # Loop through the current term to count occurrences of each digit
        for i in range(1, len(term)):
            if term[i] == term[i-1]:
                count += 1  # Increment count if the current digit is the same as the previous one
            else:
                next_term += str(count) + term[i-1]  # Append count and the digit to the next term
                count = 1  # Reset count for the new digit
        next_term += str(count) + term[-1]  # Append the count and digit for the last digit group
        term = next_term  # Update term to the next term for the next iteration
