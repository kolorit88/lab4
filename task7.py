def palindrome(text):
    text = text.lower().replace(' ', '')
    if text == text[::-1]:
        return "Палиндром"
    return "Не палиндром"

print(palindrome("А роза упала на лапу Азора"))
print(palindrome("Палиндром"))