# Write a python program that generates the first n numbers in the Fibonacci sequence. 
n=int(input("Enter the number:"))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibo = [0, 1]  
    for i in range(2, n):
        next_fib = fibo[-1] + fibo[-2]
        fibo.append(next_fib)

    print("The first",n,"numbers in fibonacci sequence are",fibo)
    
