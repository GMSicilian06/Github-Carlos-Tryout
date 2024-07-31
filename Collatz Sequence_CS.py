
def print_collatz_sequence(n):
    if n <= 0:
        print("The input must be a positive integer.")
        return
    
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    # Print the last element of the sequence

# Replace 'num' with the number you want to find the Collatz sequence for
num = 58

print_collatz_sequence(num)