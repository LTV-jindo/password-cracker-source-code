import itertools
import string
import time

# Character set
ALPHABET = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    "-_.!@#$%^&*=+;:,.<>?{}"
)

password = input("Enter a password to test:\n")

start = time.time()
counter = 0
max_length = 16

for length in range(1, max_length + 1):

    print(f"\nTrying {length}-character passwords...")

    for guess_tuple in itertools.product(ALPHABET, repeat=length):
        counter += 1

        # Much faster than converting tuple to string and replacing characters
        guess = "".join(guess_tuple)

        if guess == password:
            elapsed = time.time() - start

            print("\nPassword found!")
            print(f"Password : {guess}")
            print(f"Attempts : {counter:,}")
            print(f"Time     : {elapsed:.25f} seconds")
            print(f"Speed    : {counter / elapsed:,.0f} guesses/sec")
            exit()

    elapsed = time.time() - start
    print(f"Checked {counter:,} guesses")
    print(f"Average speed: {counter / elapsed:,.0f} guesses/sec")

print("Password not found.")