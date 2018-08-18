def sample_key_arguments(fix1, fix2, **kargs):
    print 'fixed part', fix1, fix2
    for k, v in kargs.items():
        print 'key=', k, 'value=', v


sample_key_arguments(1, 100, course='BDPY', duration=35)
a4 = {'course': 'BDPY', 'duration': 35}
sample_key_arguments(2, 'second', **a4)
