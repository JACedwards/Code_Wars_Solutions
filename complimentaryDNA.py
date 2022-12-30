# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

#works
# def DNA_strand(dna):

#     output = ''
#     for d in dna:
#         if d == 'A':
#             output = f'{output}T'
#         elif d == 'T':
#             output = f'{output}A'
#         elif d == 'C':
#             output = f'{output}G'
#         elif d == 'G':
#             output = f'{output}C'

#     return output

# print(DNA_strand("ATTGC"))

#Dictionary Version

def DNA_strand(dna):

    one = ['A','T','C','G']
    two = ['T', 'A', 'G', 'C']

    dct = {one[i]:two[i] for i in range(len(one))}
    
    output = ''
    for d in dna:
        output = f'{output}{dct.get(d)}'

    return output

print(DNA_strand("ATTGC"))

