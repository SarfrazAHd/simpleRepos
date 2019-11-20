
def reverse_of_digit(n):

    reverse = 0
    count = 0

    while n > 0:
        rem = n % 10
        reverse = reverse * 10 + rem
        n = n//10
        count += 1
    return reverse


def reverse_of_string(x):

    new_string = ''
    for i in x:
        new_string = i + new_string
    return new_string

















