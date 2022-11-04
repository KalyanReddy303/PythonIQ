def palindrome(a):
    strrev = a[::-1]
    if a == strrev:
        print(f'{a} is a palindrome')
    else:
        print(f'{a} is not a palindrome')


palindrome("tomato")
