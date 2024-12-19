def narcissistic(value):    
    # Steps
    # Get number of digits in provided value
    list_of_digits = list((str(value)))    
    num_of_digits = len(list_of_digits)
    
    # Create a product list
    digit_products = []
    
    # Create loop that iterates over each number . 
    for i in range(num_of_digits):
        current_digit = list_of_digits[i]
        # print(i + 1)
        # Muliply digit by itelf by num_of_digits
        digit_product = 1
        for i in range(num_of_digits):
            digit_product = digit_product * int(current_digit)
        digit_products.append(digit_product)


    # Display our calculated data
    print(f"Value provided: {value}")
    print(f"Number of digits: {num_of_digits}")
    print(f"List of digits: {list_of_digits}")    
    print(f"List of products of each digit to the power of {num_of_digits}: {digit_products}")

    # Add up the products
    final_sum = sum(map(int, digit_products))
    print(f"final_sum of products is {final_sum}")

    if final_sum == value:
        print(f"Value {value} is narcissistic")
        return True
    else:
        print(f"Value {value} is NOT narcissistic")
        return False

# User solutions

def narcissistic_2( value ):
    return value == sum(int(i) ** len(str(value)) for i in str(value))

# Driver
if __name__ == "__main__":
    print(narcissistic(7))
    print(narcissistic(153))
    print(narcissistic(122))
    print(narcissistic(4887))

    print(narcissistic_2(153))