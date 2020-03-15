def first_person():
    print( "First Person!")
    
    
def code_maker(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output


first_person();
result = code_maker("Sri madhava reddy ketireddy");

print (result);