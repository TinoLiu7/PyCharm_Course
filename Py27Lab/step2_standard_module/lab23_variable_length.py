def sample_variable_arguments(fix1, fix2, *args):
    print 'fixed part=', fix1, fix2
    for arg in args:
        print 'got arguments:', arg


sample_variable_arguments('1', 100, 'hello', 'world', 123)
sample_variable_arguments('2', 0.2, 'welcome', 3.14, 123, 2968)
a1 = ('hello', 'world', 123)
a2 = ['welcome', 3.14, 123, 2968]
sample_variable_arguments(3, 'three', a1)
sample_variable_arguments(4, '4th', a2)
sample_variable_arguments(3, 'three', *a1)
sample_variable_arguments(4, '4th', *a2)
a3 = {1, 1, 2, 2, 3, 3, 3, 'A', 'A', 'Hello', 'Hello'}
sample_variable_arguments(5, '5th', *a3)
a4 = {'course': 'BDPY', 'duration': 35}
sample_variable_arguments(6, '6th', *a4)
