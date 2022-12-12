def last_char(name):
    return name[-1]

print(last_char("harshit"))
#last_char(9) # error

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_even(9))

def is_even(num):
    if num%2==0:
        return True
    return False

def song():
    return "happy birthday song"
print(song())