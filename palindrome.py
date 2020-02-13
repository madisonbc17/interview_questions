#palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g., madam or nurses run (or kayak)
#^ from google dictionary

#here is a test case that can be run and expounded on as needed
def test_palindrome_validity():
    word = "madam"
    if palindrome_check(word):
        print("Success!")
    else:
        print("Fail.")

def reverse_word(word):
    reversed_word = ""
    letters = []

    for i in str(word):
        letters.append(i)

    for j in letters:
        if reversed_word == "":
            reversed_word = j
        else:
            reversed_word = j + reversed_word
    return reversed_word

def palindrome_check(word):
    reversed_word = reverse_word(word)
    
    if reversed_word == word:
        return True
    else:
        return False

#here is the "main" part of my program
test_palindrome_validity()

word = "mary"
if palindrome_check(word):
    #result is unclear, for now I will simply return "[Word] is a palindrome!"
    print(str(word) + " is a palindrome!")
else:
    print(str(word) + " is not a palindrome.")