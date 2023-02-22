def is_integer(name_prod):
    if name_prod % 2 == 0:
        return 'Ok'
    else:
        return 'No'

print(is_integer(2))