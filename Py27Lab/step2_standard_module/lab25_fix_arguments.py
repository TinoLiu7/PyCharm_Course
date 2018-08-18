def fix_argument_function(fix1, fix2, fix3):
    print fix1, fix2, fix3
    pass


fix_argument_function('a', 'b', 'c')
a1 = ('p', 'q')
fix_argument_function('X', *a1)
a2 = ['i', 'j', 'k']
fix_argument_function(*a2)
