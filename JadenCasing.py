# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    string = string.split()
    out_list = []
    out_string = ''
    
    for w in string:
        if "'" in w:
            index = w.index("'")
            w = f"{w[:index+1].title()}{w[index+1:]}"
            out_list.append(w)

        else:
            out_list.append(w.title())

    outstring = ' '.join(out_list)
    return outstring


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))