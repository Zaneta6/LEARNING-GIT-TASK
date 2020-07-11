# Function, which tells whether a word is a palindrome or not

def palindrome(word):
  print(bool(word == word[::-1]))
palindrome("SUMMER")