def to_camel_case(text):
    
    if "-" and "_" in text:
        output = text.replace("-", " ")
        output = output.replace("_", " ")
    
    elif "-" in text:
       output = text.replace("-", " ")
    #    print(output)
    elif "_" in text:
       output = output.replace("_", " ")
    #    print(output)
    else:
        return ""

    output = output.split(" ")
    print(output)

 #seems to be working up to this point
 # 
 # 
 #    
    camel = [output[0]]
    print(camel)

    for c in output[1:]:
       print(c)
       c = c.title()
       camel.append(c)

    cc = ''.join(camel)
    
    return str(cc)



print(to_camel_case('A-B_C'))

# def to_camel_case(text):
    
#     if "-" or "_" in text:
#        output = text.split("-")
#     else:
#         return ''
       
#     camel = [output[0]]

#     for c in output[1:]:
#        c = c.title()
#        camel.append(c)

#     cc = ''.join(camel)
    
#     return str(cc)

# a = 'A-B-C'
# output = a.split("-")
# print(output)