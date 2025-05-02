def palindrome(s: str) -> True:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


print(palindrome("dad"))
