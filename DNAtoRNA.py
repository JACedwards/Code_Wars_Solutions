def dna_to_rna(dna):
    output = ''

    for l in dna:
        if l == 'T':
            l = 'U'
            output = output + l
        else:
            output = output + l

    return output



print(dna_to_rna('GCAT'))