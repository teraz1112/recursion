def generateAlphabet(firstAlphabet,secondAlphabet):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if alphabet.index(firstAlphabet.lower()) > alphabet.index(secondAlphabet.lower()):
        firstAlphabet,secondAlphabet = secondAlphabet,firstAlphabet
    return alphabet[alphabet.index(firstAlphabet.lower()):alphabet.index(secondAlphabet.lower())+1]
