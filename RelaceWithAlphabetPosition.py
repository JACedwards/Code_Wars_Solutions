# found exact solution on web.  would have been plagiarism to use.
# so didn't submit to code wars.


# def alphabet_position(text):
    
#     # output = ''

#     for char in text:
#         print(ord(char))




# print(alphabet_position("The s"))

# answer = "20 8 5 19"


from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

text = "The s"

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)

print(alphabet_position("The s"))
