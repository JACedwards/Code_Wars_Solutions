# Given a word w and some text t, find whether w is in t. For example: w="nest", t="I built a nest and tested it."

def includes(w, t):

    x = t.split()
    for y in x:
        if y == w:
            return True
        
    return False





print(includes("nest", "I built a nest and tested it."))
