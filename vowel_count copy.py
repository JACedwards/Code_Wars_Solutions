def vowel(sentence):
    
    num = 0
    v = ['a', 'e', 'i', 'o', 'u']
    
    for char in sentence:
        if char in v:
            num = num + 1
        else:
            continue
            
    return num

print(vowel('booty'))

