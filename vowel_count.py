
def vowel_count(sentence):
    """Counts vowels in a string"""

    count = 0
    v = ['a','e','i','o','u']

    for char in sentence:
        if char in v:
            count = count + 1
        else:
            continue
            
    return count
         

print(vowel_count(''))