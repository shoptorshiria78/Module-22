# Function to calculate the number of digits in a number
def calculate_length(n):
    return len(str(n))

# Function to check if a number is a Disarium number
def is_disarium(num):
    length = calculate_length(num)
    temp = num
    sum_of_digits = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** length
        length -= 1
        temp //= 10
    
    return sum_of_digits == num

# Main program
number = int(input("Enter a number: "))

if is_disarium(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")
