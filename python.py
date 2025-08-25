# task.py

# 1. Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. String palindrome check
def is_palindrome(s):
    return s == s[::-1]

# 3. Anagram check (two strings)
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


# Testing
if name == "main":
    print("Prime Check:")
    print("7 ->", is_prime(7))
    print("10 ->", is_prime(10))

    print("\nPalindrome Check:")
    print("madam ->", is_palindrome("madam"))
    print("hello ->", is_palindrome("hello"))

    print("\nAnagram Check:")
    print("listen & silent ->", is_anagram("listen", "silent"))
    print("hello & world ->", is_anagram("hello", "world"))