def is_pronic(n):
    "Checks if a number is pronic."
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    return False

def find_pronic_in_substring(string):
    "Finds pronic numbers in a substring."
    pronic_numbers = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring.isdigit() and is_pronic(int(substring)):
                pronic_numbers.append(int(substring))
    return pronic_numbers


string = input("Enter Number: ")
print(find_pronic_in_substring(string))