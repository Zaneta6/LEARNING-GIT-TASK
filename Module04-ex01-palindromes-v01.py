# Function, which tells whether a word is a palindrome or not

def palindrome(word):
  return bool(word == word[::-1])
print(palindrome("SUMMER"))