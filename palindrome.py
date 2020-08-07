def palindrome(string):
    """A palindrome is a word, number, phrase,
    or other sequence of characters which reads
    the same backward as forward, such as madam,
    racecar. There are also numeric palindromes,
    including date/time stamps using short digits
     11/11/11 11:11 and long digits 02/02/2020."""
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])


if __name__ == '__main__':
    print(palindrome("abba"))
