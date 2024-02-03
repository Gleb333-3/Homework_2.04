word = "comprehension"
consostant = ["a", "e", "o", "u", "i"]
#9.1
letter_count = {letter: word.count(letter) for letter in word}
print(letter_count)
#9.2
letter_count = {letter: word.count(letter) for letter in word if letter.isalpha() and letter not in consostant }
print(letter_count)