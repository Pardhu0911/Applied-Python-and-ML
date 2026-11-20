import math

# --- LOGIC EXPLANATION ---
# The isPrime(n) function uses a mathematical optimization to check for primality.
# It iterates from 2 up to the square root of n. If n is divisible by any of these 
# numbers, it is not prime. This is efficient because if no factor is found 
# by the square root, no factor exists at all.

def isPrime(n):
    """Checks if a number is prime by testing factors up to the square root."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- EXTENDED LOGIC ---
# To find the specific range of primes (9991 to 10000), I used a counter 
# and a while loop. Efficiency is improved using 'continue' and 'break'.

primes_list = []
candidate = 2
count = 0

while count < 10000:
    # EFFICIENCY: Skip even numbers (except 2) using 'continue' to save processing time.
    if candidate > 2 and candidate % 2 == 0:
        candidate += 1
        continue 
    
    if isPrime(candidate):
        count += 1
        
        # Only collect the primes that fall within our target range
        if count >= 9991:
            primes_list.append(candidate)
            
        # EFFICIENCY: Use 'break' to stop immediately once the 10,000th prime is found.
        if count == 10000:
            break
            
    candidate += 1

# Display results
print("Primes from 9991st to 10000th:", primes_list)

# Output the numbers to prime.txt as required
with open("prime.txt", "w") as f:
    for p in primes_list:
        f.write(str(p) + "\n")

"""
To make the code run faster and meet the assignment requirements, I used continue and break:

continue: I used this to skip even numbers. Since 2 is the only even prime, it’s a waste of time to check numbers like 4, 6, or 8. By using continue, the program jumps back to the start of the loop as soon as it sees an even number, which saves a lot of work.

break: I used this to stop the loop. As soon as my counter hit 10,000, I didn't need to check any more numbers. Using break kills the loop instantly so the computer doesn't keep running for no reason."""
