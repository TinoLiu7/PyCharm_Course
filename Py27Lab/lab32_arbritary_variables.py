def sample_variable_arguments(fix1, fix2, *args):
    print "fix part1=%s, part2=%s" % (str(fix1), str(fix2))
    for arg in args:
        print "variable=%s" % arg
        pass
    pass


sample_variable_arguments("hello", "world", 3, 4.5, "678", 'kk')
l1 = [3, 4.5, "678", 'kk']
sample_variable_arguments("hello", "l1 in list", l1)
sample_variable_arguments("hello", "l1 in list", *l1)
l2 = (3, 4.5, "678", 'kk')
sample_variable_arguments("hello", "l2 in tuple", *l2)
l3 = {3, 4.5, "678", 'kk'}
sample_variable_arguments("hello", "l3 in set", *l3)
l4 = {'name': 'python in action', 'duration': '16hr'}
sample_variable_arguments("hello", 'l4 in dict', *l4)
l4 = {'name': 'python in action', 'duration': '16hr'}
sample_variable_arguments("hello", 'values of l4 in dict',
                          *(l4.values()))
