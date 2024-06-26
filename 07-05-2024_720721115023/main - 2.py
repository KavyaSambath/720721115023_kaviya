def is_palindrome(x: int) -> bool:
    if x < 0: 
        return False
    original_x = x 
    reversed_x = 0 
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    return original_x == reversed_x 
x = 141
print(is_palindrome(x))
x = -141
print(is_palindrome(x))
x = 40
print(is_palindrome(x))
