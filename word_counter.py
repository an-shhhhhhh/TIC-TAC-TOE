def word_counter(s):
    em={}
    for char in s:
        total=s.count(char)
        em[char]=total
    return print(em)
word_counter("anshika")