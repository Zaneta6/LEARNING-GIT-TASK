def palindrome(word):
  if word == word[::-1]:
    print("True" + '\n' + f"The word {word} is a palindrome.")
  else:
    print("False" + '\n' + f"The word {word} is not a palindrome")
palindrome("SUMMER")