# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
class Camel():

    def __init__(self, s) -> None:
        self.s = s
    
    def solution(self):

        output = ''

        for c in self.s:

            if c.isupper() == False:
                output = f"{output}{c}"
            else: 
                output = f"{output} {c}"

        return output

camel1 = Camel("camelCasing")

print(camel1.solution())