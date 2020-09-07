def reverseString(string: str): # METHOD - 2
    # return string[::-1] # METHOD - 1
    revString = ''
    for i in string:
        revString = i+revString
    return revString


def reverseStringRecusrsively(string: str): # METHOD -3
    if len(string) <= 1:
        return string
    return reverseStringRecusrsively(string[1:]) + string[0]


if __name__ == "__main__":
    print(reverseStringRecusrsively('awesome'))
    print(reverseStringRecusrsively('aw'))
    print(reverseString('awesome'))
    print(reverseString('aw'))
