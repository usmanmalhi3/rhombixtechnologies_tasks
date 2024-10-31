def fibonacci(n):
   
    
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    elif n == 2:
        return [0, 1]  

    fib_sequence = [0, 1]  
    for _ in range(2, n):
       
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)  
    return fib_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        fib_sequence = fibonacci(n)
        print(f"The first {n} terms of the Fibonacci sequence are: {fib_sequence}")
    except ValueError:
        print("Please enter a valid integer.")


main()
