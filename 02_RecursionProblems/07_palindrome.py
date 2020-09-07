# Check if a String is palindrome or not

def isPalindrome_1(string: str):  # METHOD - 1
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            print('"{}" is not a palindrome'.format(string))
            break
        start += 1
        end -= 1
    else:
        print('"{}" is a palindrome'.format(string))


def isPalindromeRecursive(string: str):  # METHOD - 2
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    elif string[0] == string[:-1]:
        return isPalindromeRecursive(string[1:-1])
    else:
        return False


if __name__ == "__main__":
    isPalindrome_1('awesome')
    isPalindrome_1('foobar')
    isPalindrome_1('tacocat')
    isPalindrome_1('amanaplanacanalpanama')
    isPalindrome_1('amanaplanacanalpandemonium')
    # METHOD - 2
    print(isPalindromeRecursive('awesome'))
    print(isPalindromeRecursive('foobar'))
    print(isPalindromeRecursive('tacocat'))
    print(isPalindromeRecursive('amanaplanacanalpanama'))
    print(isPalindromeRecursive('amanaplanacanalpandemonium'))