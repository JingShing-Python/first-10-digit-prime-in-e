import time
# google question
# first 10-digit prime found in consecutive digits of e
def is_prime(n):
    # determine prime
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_first_prime_position(digits:str, window_size:int)->None:
    # find first 10-digit prime
    # get content and digit that want to determine
    for i in range(len(digits) - window_size + 1):
        sub_digits = digits[i:i+window_size]
        number = int(sub_digits)
        if is_prime(number):
            print(f"first 10-digit prime: {sub_digits}")
            print(f"find pos: {i + 1}")
            return
    print("not found!")
    return

import time

if __name__ == "__main__":
    start_time = time.time()
    # file name of euler's number
    filename = "e_2mil.txt"
    with open(filename, "r") as file:
        content = file.read().replace('\n', '')
    # delete all not number elements
    digits = ''.join(filter(str.isdigit, content))
    # find 10-digit
    window_size = 10
    find_first_prime_position(digits, window_size)
    end_time = time.time()
    print("total time: " + str(end_time - start_time) + " seconds")
