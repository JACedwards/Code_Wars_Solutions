# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

#Pseudo code:
    # strip leading/ending spaces
    # split string at word breaks (3 spaces)
    # split each string in this list into list of code characters
    # loop through list, replacing code with letters using dictionary
    # join list into word
    # join words into sentence

def decode_morse(morse_code):
    #this dictionary only has letters and numbers, no other characters
    MORSE_CODE = {".-": "A",
          "-...": "B",
          "-.-.": "C",
          "-..": "D",
          ".": "E",
          "..-.": "F",
          "--.": "G",
          "....": "H",
          "..": "I",
          ".---": "J",
          "-.-": "K",
          ".-..": "L",
          "--": "M",
          "-.": "N",
          "---": "O",
          ".--.": "P",
          "--.-": "Q",
          ".-.": "R",
          "...": "S",
          "-": "T",
          "..-": "U",
          "...-": "V",
          ".--": "W",
          "-..-": "X",
          "-.--": "Y",
          "--..": "Z",
          "-----": "0",
          ".----": "1",
          "..---": "2",
          "...--": "3",
          "....-": "4",
          ".....": "5",
          "-....": "6",
          "--...": "7",
          "---..": "8",
          "----.": "9"}
    split_word_list = []
    
    morse_code = morse_code.strip()
    split_sent = morse_code.split('   ')

    for w in split_sent:
        split_word = w.split()
        split_word_list.append(split_word)
    
    translate = ''
    translated_list = []
    for word in split_word_list:
        for char in word:
            translate = f"{translate}{MORSE_CODE.get(char)}"
        translated_list.append(translate)
        translate = ''

    output = ' '.join(translated_list)
    return output
        
print(decode_morse('    .... . -.--   .--- ..- -.. .     '))

