#Q1
def iterativevowels(value):
    total = 0
    lengthstring = len(value)
    for x in range(lengthstring):
        firstchar = value[0].lower()
        if firstchar == 'a' or firstchar == 'e' or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':
            total = total + 1
        value = value[1:lengthstring]
    return total
print(iterativevowels('house'))

def recursivevowel(value):
    if len(value) == 0:
        return 0
    else:
        firstchar = value[0].lower()
    if firstchar == 'a' or firstchar == 'e' or firstchar == 'i' or firstchar == 'o' or firstchar == 'u':
        return 1 + recursivevowel(value[1:len(value)])
    else:
        return recursivevowel(value[1:len(value)])
#takyah total dh, return 1 + recursive lagi skali
print(recursivevowel('imagine'))

#print one part only
value = 'hai'
print(value[0]) #first char
print(value[0:3]) #first until what
