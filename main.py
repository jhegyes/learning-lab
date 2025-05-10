def prime_check():
    while True: # infinite loop until break occurs
        factors = []
        a = input("Enter a number (or type 'exit' to quit): ")
        if a.lower() == "exit":
            print("Good bye!")
            break

        try: # try and exception block
            b=int(a)
            if b < 2:
                print(f"{b} is not prime.")
                continue # back to the beginning of the loop

            for i in range (2, int(b ** 0.5) + 1): # loop from 2 to 1 plus square root of input
                # print(f"factoring {i}") # optional debug line
                if b % i == 0: # % returns remainder of division
                    print(f"{b} is not prime")
                    print(f"Here are the factors of {b}:")
                    for j in range (1, b // 2 + 1):  # testing factors up to half the input, // means integer of division output 
                        if b%j == 0:
                            factors.append(j)
                            print(j)
                    print(b)
                    factors.append(b) # including the input at the end as a factor of itself
                    print(factors)
                    print(f"I have counted {len(factors)} factors of {b}.")
                    break         
            else: # else runs only if for loop completes without a break
                print(f"{b} is prime")                    
        except ValueError:
            print("Please enter a valid number.")

prime_check()
