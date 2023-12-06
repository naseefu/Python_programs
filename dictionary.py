def monotoneIncreasingDigits(n):
    digits = list(str(n))
    length = len(digits)
    
    # Find the first digit from the left that violates the monotone increasing condition
    i = 1
    while i < length and digits[i - 1] <= digits[i]:
        i += 1
    
    # If no violation was found, the number is already monotone increasing
    if i == length:
        return n
    
    # Decrement the violating digit and set all digits to its right to 9
    while i > 0 and digits[i - 1] > digits[i]:
        digits[i - 1] = str(int(digits[i - 1]) - 1)
        i -= 1
    
    # Set all digits to the right of the violating digit to 9
    for j in range(i + 1, length):
        digits[j] = '9'
    
    # Convert the list of digits back to an integer
    return int(''.join(digits))

# Example usage:
print(monotoneIncreasingDigits(10))    # Output: 9
print(monotoneIncreasingDigits(1243))  # Output: 1234
print(monotoneIncreasingDigits(332))   # Output: 299
