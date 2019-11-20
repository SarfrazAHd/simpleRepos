



x = "My name is"



def number_of_vowel(x):
    vowel = 0
    space = 0
    for i in range(len(x)):
        if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
            vowel += 1
        else:
            if x[i] == " ":
                space += 1

    return vowel, len(x)-vowel-space

print(number_of_vowel(x))