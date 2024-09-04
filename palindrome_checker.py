def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]
#example usage
word="Racecar"
#checking and printing the word
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")