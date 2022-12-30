# Task
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

# Input:

# If, you can read?

# Output:

# India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

# Note:

# There are preloaded dictionary you can use, named NATO
# The set of used punctuation is ,.!?.
# Punctuation should be kept in your return string, but spaces should not.
# Xray should not have a dash within.
# Every word and punctuation mark should be seperated by a space ' '.
# There should be no trailing whitespace

#Psuedo:
#For loop through string
#if character letter:
#    concatinate using NATO dictionary
#         with LEADING space
#if character in punctuation list:
#    contcatinate punctuation mark
#           with LEADING
#else: have a space and shouldn't need to do anything?
#strip leading space
#return


def to_nato(words):
    punct = [',', '.', '!', '?']
    output = ''
    nato = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu']
    alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nato_dict = {alphab[i] : nato[i] for i in range(len(alphab))}

    for c in words:
        if c.isalpha():
            output = f"{output} {nato_dict.get(c.lower())}"
        if c in punct:
            output = f"{output} {c}"
    return output.strip()



print(to_nato('Did not see that coming'))