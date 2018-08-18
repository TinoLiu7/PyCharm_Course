def getDigit(x):
    """

    :type x: int or float
    """
    returnDigit = 0
    while x > 0:
        x //= 10
        returnDigit += 1
    return returnDigit


print getDigit("123456789012345678901234567890")
