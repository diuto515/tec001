def acronym(phrase):
    return "".join(word[0].upper() for word in phrase.split())

print(acronym("unidentified foreign object"))  